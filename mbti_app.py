import json
import sys
import os

class MBTIDiagnosis:
    def __init__(self, questions_path='questions.json'):
        self.questions_path = questions_path
        self.questions = self._load_questions()
        self.scores = {
            'E': 0, 'I': 0,
            'S': 0, 'N': 0,
            'T': 0, 'F': 0,
            'J': 0, 'P': 0
        }
        self.descriptions = {
            "INTJ": "建築家: 想像力が豊かで、戦略的な思考の持ち主。あらゆることに計画を立てます。",
            "INTP": "論理学者: 貪欲な知識欲を持つ革新的な発明家。理論的な分析を好みます。",
            "ENTJ": "指揮官: 大胆で想像力豊かなリーダー。常に道を見つめるか、道を作ります。",
            "ENTP": "討論者: 賢くて好奇心旺盛な思考家。知的挑戦を無視できないタイプです。",
            "INFJ": "提唱者: 静かで神秘的だが、人々を非常に勇気づける理想主義者。",
            "INFP": "仲介者: 詩人肌で親切な利他主義者。良い物事のためなら、いつでも手を差し伸べます。",
            "ENFJ": "主人公: カリスマ性があり、人々を励ますリーダー。聞く人を魅了します。",
            "ENFP": "広報運動家: 情熱的で独創力があり、かつ社交的な自由人。常に笑いを見つけられます。",
            "ISTJ": "管理者: 実用的で事実に基づいた思考を持つ、非常に信頼できる個人。",
            "ISFJ": "擁護者: 非常に献身的で心の温かい擁護者。いつでも愛する人を守る準備ができています。",
            "ESTJ": "幹部: 優れた管理者で、物事や人々を管理する能力に長けています。",
            "ESFJ": "領事官: 非常に思いやりがあり社交的で、人気がある。常に助けようとしてくれます。",
            "ISTP": "巨匠: 大胆で実践的な実験者。あらゆる道具を使いこなします。",
            "ISFP": "冒険家: 柔軟で魅力がある芸術家。常に新しいことを経験する準備ができています。",
            "ESTP": "起業家: 賢く、エネルギッシュで、非常に鋭い知覚を持つ。危険な道も厭いません。",
            "ESFP": "エンターテイナー: 自発的でエネルギッシュ、熱心なエンターテイナー。周りを退屈させません。"
        }

    def _load_questions(self):
        if not os.path.exists(self.questions_path):
            print(f"Error: {self.questions_path} not found.")
            sys.exit(1)
        with open(self.questions_path, 'r', encoding='utf-8') as f:
            return json.load(f)

    def run_test(self):
        print("=== MBTI診断プログラム (100問版) ===")
        print("1: 全く当てはまらない")
        print("2: あまり当てはまらない")
        print("3: どちらともいえない")
        print("4: やや当てはまる")
        print("5: 非常に当てはまる")
        print("-" * 30)

        for i, q in enumerate(self.questions):
            while True:
                try:
                    answer = input(f"Q{i+1}/{len(self.questions)}: {q['question']} (1-5): ")
                    val = int(answer)
                    if 1 <= val <= 5:
                        break
                    print("1から5の間で入力してください。")
                except ValueError:
                    print("数字を入力してください。")

            # Scoring logic:
            # 3 (neutral) adds 0 to both.
            # 4, 5 adds weight to the 'direction'
            # 1, 2 adds weight to the opposite 'direction'
            weight = val - 3
            dim = q['dimension']
            target = q['direction']
            
            # Identify opposite
            if dim == 'EI': opposite = 'E' if target == 'I' else 'I'
            elif dim == 'SN': opposite = 'S' if target == 'N' else 'N'
            elif dim == 'TF': opposite = 'T' if target == 'F' else 'F'
            elif dim == 'JP': opposite = 'J' if target == 'P' else 'P'

            if weight > 0:
                self.scores[target] += weight
            elif weight < 0:
                self.scores[opposite] += abs(weight)

    def get_result(self):
        mbti = ""
        mbti += 'E' if self.scores['E'] >= self.scores['I'] else 'I'
        mbti += 'S' if self.scores['S'] >= self.scores['N'] else 'N'
        mbti += 'T' if self.scores['T'] >= self.scores['F'] else 'F'
        mbti += 'J' if self.scores['J'] >= self.scores['P'] else 'P'
        
        description = self.descriptions.get(mbti, "詳細な説明が見つかりませんでした。")
        return mbti, description

    def show_summary(self):
        mbti, desc = self.get_result()
        print("\n" + "=" * 30)
        print(f"診断結果: {mbti}")
        print(f"{desc}")
        print("=" * 30)
        print("\nスコア詳細:")
        print(f"E-I: E {self.scores['E']} - I {self.scores['I']}")
        print(f"S-N: S {self.scores['S']} - N {self.scores['N']}")
        print(f"T-F: T {self.scores['T']} - F {self.scores['F']}")
        print(f"J-P: J {self.scores['J']} - P {self.scores['P']}")

if __name__ == "__main__":
    app = MBTIDiagnosis()
    try:
        app.run_test()
        app.show_summary()
    except KeyboardInterrupt:
        print("\n中断されました。")
