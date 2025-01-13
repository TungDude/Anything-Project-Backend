from flask import jsonify

class APIHelper():
    def test_api():
        return jsonify({
            "status": "success", 
            "Test": "Hello Word", 
        })