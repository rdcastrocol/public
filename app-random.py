from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de imágenes (pares)
images = [
    "imagen1.jpg", "imagen1.jpg",
    "imagen2.jpg", "imagen2.jpg",
    # Agrega más imágenes según sea necesario
]

# Organizar las imágenes de manera aleatoria
random.shuffle(images)

@app.route('/')
def index():
    return render_template('memory_game.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)
