import os

RULES_DIR = "analytics-rules"

def validate_kql_file(file_path):
    with open(file_path, 'r') as f:
        content = f.read().strip()
        if not content:
            print(f"❌ Rule {file_path} is empty.")
            return False
        else:
            print(f"✅ Rule {file_path} looks valid (simulated).")
            return True

def simulate_validation():
    print("🔍 Simulating Sentinel rule validation...")
    all_passed = True
    for filename in os.listdir(RULES_DIR):
        if filename.endswith(".kql"):
            full_path = os.path.join(RULES_DIR, filename)
            if not validate_kql_file(full_path):
                all_passed = False
    return all_passed

if __name__ == "__main__":
    success = simulate_validation()
    if not success:
        print("❌ Simulation failed. Fix issues and try again.")
        exit(1)
    print("🎉 All rules passed simulated validation.")
