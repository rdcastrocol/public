from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de imágenes (pares)
images = [
    "image1.jpg", "image1.jpg",
    "image2.jpg", "image2.jpg",
    "image3.jpg", "image3.jpg",
    "image4.jpg", "image4.jpg",
    "image5.jpg", "image5.jpg",
    "image6.jpg", "image6.jpg",
    "image7.jpg", "image7.jpg",
    "image8.jpg", "image8.jpg",
    # Agrega más imágenes según sea necesario
]

# Asegurar que hay suficientes imágenes
if len(images) % 2 != 0:
    raise ValueError("Número impar de imágenes. Asegúrate de tener pares de imágenes.")

# Organizar las imágenes de manera aleatoria
random.shuffle(images)

@app.route('/')
def index():
    return render_template('memory_game.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
