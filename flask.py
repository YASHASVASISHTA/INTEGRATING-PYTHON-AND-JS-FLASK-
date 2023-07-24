from flask import Flask, jsonify
import ideagenerator  # Replace with the actual name of your hackathon idea generation code

app = Flask(__name__)

@app.route('/get_idea', methods=['GET'])
def get_hackathon_idea():
    idea = ideagenerator.scrape_hackathon_ideas()  # Replace with the actual function to generate ideas
    return jsonify({'idea': idea})

if __name__ == '__main__':
    app.run()
