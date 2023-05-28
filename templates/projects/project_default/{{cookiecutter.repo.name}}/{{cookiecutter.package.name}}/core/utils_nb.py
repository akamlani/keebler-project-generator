from IPython.display import Markdown
from tqdm.autonotebook import tqdm


def render_text_markdown(text:str) -> IPython.core.display.Markdown:
    return Markdown(text)