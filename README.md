# QuickQuizzAI

Ever found yourself struggling to engage with your reading materials? What if there was a way to supercharge your learning experience using the power of AI? This project integrates various technologies to facilitate effortless learning from a wide range of text sources. Simply upload a picture of the reading and whether it be a physical textbook under low lighting or a screenshot from an online pdf, QuickQuizzAI will generate an engaging and pertanent question to reinforce your reading. 

Python serves as the foundation for its functionality. OpenCV, a computer vision library, is employed for image manipulation and preprocessing, enabling the system to process images from diverse sources, including online textbook screenshots and low-quality book images.

Optical Character Recognition (OCR) technology, specifically Tesseract, is used to extract text from images. OCR plays a critical role in converting scanned book pages and images into machine-readable text, making educational content accessible.

The ChatGPT API, powered by a large language model, generates questions related to the extracted text. It automates the creation of quizzes, facilitating interactive learning experiences. Finally, the project is hosted on Gradio, an interactive interface platform for Python machine learning models, ensuring user-friendliness and accessibility. In summary, this project combines Python, OpenCV, OCR (Tesseract), ChatGPT, and Gradio to make learning from text images seamless and adaptable to various sources and quality levels.
