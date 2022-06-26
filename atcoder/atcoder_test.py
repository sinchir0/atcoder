def _preinput(input_text: str):
    out = input_text.split("\n")

    # 最初が改行の場合は飛ばす
    if out[0] == "":
        out = out[1:]
    # 最後が改行の場合は飛ばす
    if out[-1] == "":
        out = out[:-1]

    for i in out:
        yield i


def input(reset: bool = False):
    global input_text, inp
    if reset:
        del inp, input_text, repeat
        return
    try:
        return inp.__next__()
    except:
        raise ValueError("error!")


def def_input(s: str, isRepeat=False):
    global input_text, inp, repeat
    input_text = s
    repeat = isRepeat
    inp = _preinput(input_text)
