from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-spam', methods=['POST'])
def check_spam():
    data = request.get_json()
    message = data.get('message', '').lower()

    spam_keywords = ["win money", "free", "credit card", "click here", "urgent", "act now", "prize", "lottery", "buy now"]
    is_spam = any(word in message for word in spam_keywords)

    return jsonify({
        "is_spam": is_spam,
        "message": "🚫 This message looks like spam." if is_spam else "✅ This message looks clean."
    })

@app.route('/check-categories', methods=['POST'])
def check_categories():
    data = request.get_json()
    message = data.get('message', '').lower()

    categories = {
        "Financial Scam": ["bank account", "credit card", "loan", "transfer funds"],
        "Advertisement": ["buy now", "limited offer", "discount", "sale"],
        "Lottery/Prize": ["you won", "claim prize", "lottery", "winner"],
        "Phishing/Urgent": ["urgent", "act now", "verify", "click link"]
    }

    detected = []
    for category, keywords in categories.items():
        if any(word in message for word in keywords):
            detected.append(category)

    return jsonify({
        "categories": detected,
        "message": (
            f"🚫 Spam Categories Detected: {', '.join(detected)}" if detected
            else "✅ No specific spam categories detected."
        )
    })

@app.route('/classify-category', methods=['POST'])
def classify_category():
    data = request.get_json()
    message = data.get('message', '').lower()

    category_keywords = {
        "Education": ["exam", "university", "school", "admission", "course", "result"],
        "Internship": ["internship", "training", "stipend", "apply now", "intern"],
        "Job Offer": ["hiring", "job offer", "vacancy", "recruitment", "resume"],
        "Finance": ["loan", "emi", "bank", "account", "investment", "credit"],
        "Promotion / Ad": ["buy now", "discount", "sale", "limited offer", "deal"]
    }

    for category, keywords in category_keywords.items():
        if any(word in message for word in keywords):
            return jsonify({ "category": category })

    return jsonify({ "category": "Other" })


if __name__ == '__main__':
    app.run(debug=True)

    
