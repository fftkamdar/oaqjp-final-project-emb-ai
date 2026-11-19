
import unittest
from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_joy(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.90,
                    "sadness": 0.04
                }
            }]
        }

        result = emotion_detector("I am happy")

        self.assertEqual(result["dominant_emotion"], "joy")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_sadness(self, mock_post):
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "emotionPredictions": [{
                "emotion": {
                    "anger": 0.01,
                    "disgust": 0.02,
                    "fear": 0.03,
                    "joy": 0.04,
                    "sadness": 0.90
                }
            }]
        }

        result = emotion_detector("I am sad")

        self.assertEqual(result["dominant_emotion"], "sadness")

    @patch("EmotionDetection.emotion_detection.requests.post")
    def test_anger(self, mock_post):
        mock_post.return_value.status_code = 400

        result = emotion_detector("")

        self.assertIsNone(result["dominant_emotion"])


if __name__ == "__main__":
    unittest.main()
