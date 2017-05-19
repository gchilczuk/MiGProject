from tinymce.models import HTMLField

def blog_body_cut(blog_body):
    new_body = str(blog_body)
    i = new_body.find('</p>')
    new_body = new_body[:i]+'</p>'
    # if new_body == '</p>': return 
    if '<p>' not in new_body:
        new_body = '<p>' + new_body
    return new_body