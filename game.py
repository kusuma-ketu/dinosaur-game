import gradio as gr

def identify_dino(images, correct_label):
    return f"the correct answer is {correct_label}"

images = [gr.Image('pil') for _ in range(4)]
interface = gr.Interface(
    fn=identify_dino,
    inputs=[gr.input.Image(label="Dinosaur Image") for _ in range(4)] + [gr.iniputs.Textbox(label='Correct Dinosaur Name')],
    outputs='text',
    live=True
)
interface.launch()