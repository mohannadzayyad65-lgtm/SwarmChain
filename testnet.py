from network import SwarmNetwork
import time

def run_testnet():
    print("🌐 بدء Local Testnet لـ SwarmChain...\n")
    
    network = SwarmNetwork()
    
    # إضافة 5 عقد
    for i in range(1, 6):
        network.add_node(f"Validator-{i}")
        time.sleep(0.3)
    
    print("\n📦 إرسال معاملات تجريبية...")
    for i in range(3):
        network.simulate_consensus([f"Tx-{i+1}: User{i} pays 10 PHERO"])
        time.sleep(1)
    
    print("\n✅ Local Testnet انتهى بنجاح!")
    print("النظام جاهز للتوسع.")

if __name__ == "__main__":
    run_testnet()
