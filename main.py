from network import SwarmNetwork
from governance import Governance
from node import Node

def main():
    print("🚀 بدء تشغيل SwarmChain...\n")
    
    # إنشاء الشبكة
    network = SwarmNetwork()
    network.add_node("Validator-A")
    network.add_node("Validator-B")
    network.add_node("Validator-C")
    
    # إنشاء كتلة أولى
    print("\n📦 إنشاء الكتلة الأولى...")
    network.simulate_consensus(["Alice pays Bob 50 PHERO"])
    
    # نظام الحوكمة
    print("\n🗳️  نظام الحوكمة:")
    gov = Governance()
    prop = gov.create_proposal("تحسين معدل التبخر", "تقليل معدل التبخر إلى 0.97")
    gov.vote(prop["id"], network.nodes[0], True)
    gov.finalize_proposal(prop["id"])
    
    print("\n✅ SwarmChain يعمل بنجاح!")
    print("النظام جاهز للاختبار على Local Testnet.")

if __name__ == "__main__":
    main()
