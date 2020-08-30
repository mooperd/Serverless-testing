from s3_bang import s3_bang

def run(event, context):
    print(event)
    print(context)
    s3_bang()


