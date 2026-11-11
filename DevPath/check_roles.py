import json

# Read the seed data file
with open('z:/demo/roadmaps/seed_data.py', 'r') as f:
    content = f.read()

# Extract the SEED_ROLES part
start_marker = "SEED_ROLES = ["
end_marker = "]"

start_idx = content.find(start_marker)
if start_idx == -1:
    print("Could not find SEED_ROLES")
    exit(1)

# Find the matching end bracket (this is tricky, so let's use a simple approach)
lines = content.split('\n')
roles_start = -1
for i, line in enumerate(lines):
    if "SEED_ROLES = [" in line:
        roles_start = i
        break

if roles_start == -1:
    print("Could not find SEED_ROLES start")
    exit(1)

# Parse the roles manually
roles = []
current_role = {}
brace_count = 0
in_role = False

for i in range(roles_start + 1, len(lines)):
    line = lines[i].strip()
    
    if line == "{":
        if not in_role:
            in_role = True
            current_role = {}
        brace_count += 1
    elif line == "},":
        brace_count -= 1
        if brace_count == 0 and in_role:
            roles.append(current_role)
            current_role = {}
            in_role = False
    elif line == "]":
        break
    elif in_role and line.startswith('"') and ':' in line:
        # Parse key-value pairs
        try:
            key, value = line.split(':', 1)
            key = key.strip().strip('"')
            value = value.strip()
            if value.startswith('[') and value.endswith(']'):
                # It's a list
                current_role[key] = []
            elif value.startswith('"') and value.endswith('"'):
                # It's a string
                current_role[key] = value.strip('"')
            elif value.isdigit():
                # It's a number
                current_role[key] = int(value)
        except:
            pass

print(f"Found {len(roles)} roles")

# Check which roles have certifications
roles_with_certs = 0
for role in roles:
    if 'certification_recommendations' in role:
        roles_with_certs += 1

print(f"Roles with certifications: {roles_with_certs}")
print(f"Roles without certifications: {len(roles) - roles_with_certs}")
