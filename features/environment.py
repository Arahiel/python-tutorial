def before_all(context):
    print("/////////////////////////Before all Hit!")


def after_all(context):
    print("/////////////////////////After all Hit!")


def before_tag(context, tag):
    print("/////////////////////////Before tag Hit!")

    if tag == "SetVarATo5":
        print("/////////////////////////Before tag (SetVarATo5) Hit!")
        context.a = 5
        print(f"SetVarATo5: {context.a}")
    elif tag == "SetVarATo7":
        print("/////////////////////////Before tag (SetVarATo7) Hit!")
        context.a = 7
        print(f"SetVarATo5: {context.a}")
    elif tag == "PrintHelloBefore":
        print("/////////////////////////Before tag (PrintHelloBefore) Hit!")
        print("Hello there!")


def after_tag(context, tag):
    print("/////////////////////////After tag Hit!")

    if tag == "PrintHelloAfter":
        print("/////////////////////////After tag (PrintHelloAfter) Hit!")
        print("Hello there!")
