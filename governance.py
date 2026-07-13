from node import Node

class Governance:
    def __init__(self):
        self.proposals = []
    
    def create_proposal(self, title: str, description: str):
        proposal = {
            "id": len(self.proposals) + 1,
            "title": title,
            "description": description,
            "votes_for": 0,
            "votes_against": 0,
            "status": "open"
        }
        self.proposals.append(proposal)
        print(f"📝 تم إنشاء اقتراح: {title}")
        return proposal

    def vote(self, proposal_id: int, node: Node, support: bool):
        for p in self.proposals:
            if p["id"] == proposal_id:
                if support:
                    p["votes_for"] += node.stake if hasattr(node, 'stake') else 100
                else:
                    p["votes_against"] += node.stake if hasattr(node, 'stake') else 100
                print(f"🗳️  {node.name} صوت {'مع' if support else 'ضد'} الاقتراح {proposal_id}")
                return
        print("❌ الاقتراح غير موجود")

    def finalize_proposal(self, proposal_id: int):
        for p in self.proposals:
            if p["id"] == proposal_id:
                total = p["votes_for"] + p["votes_against"]
                if total == 0:
                    print("لا يوجد تصويت")
                    return
                if p["votes_for"] / total > 0.66:
                    p["status"] = "approved"
                    print(f"✅ الاقتراح {proposal_id} تمت الموافقة عليه!")
                else:
                    p["status"] = "rejected"
                    print(f"❌ الاقتراح {proposal_id} تم رفضه")
                return

# مثال
if __name__ == "__main__":
    gov = Governance()
    node1 = Node("Validator-1")
    node1.stake = 10000   # إضافة Stake
    
    prop = gov.create_proposal("زيادة حجم الكتلة", "زيادة حجم الكتلة إلى 2MB")
    gov.vote(prop["id"], node1, True)
    gov.finalize_proposal(prop["id"])
