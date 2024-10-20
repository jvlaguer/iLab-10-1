from flask import Blueprint, request, jsonify
from backend.app.services.vqa_service import predict_vqa
from flask_cors import cross_origin

vqa_routes = Blueprint("vqa", __name__)


@vqa_routes.route("/vqa", methods=["POST", "OPTIONS"])
@cross_origin(
    origin="http://localhost:5173",
    methods=["POST", "OPTIONS"],
    support_credentials=True,
)
def vqa():
    if request.method == "OPTIONS":
        # This handles the preflight request by sending the correct CORS headers.
        return jsonify({"message": "CORS preflight accepted"}), 200
    image = request.files.get("image")
    question = request.form.get("question")

    # Call the VQA service to get predictions
    answer = predict_vqa(question, image)

    return jsonify({"answer": answer})
