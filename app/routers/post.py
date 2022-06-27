from fastapi import APIRouter, Request, status, Response
from fastapi.templating import Jinja2Templates
from app.schemas import Post, Reply


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


# -- Requests ------------------------------------------------------------------

@router.get("/")
def forum(request: Request):
    """ Display forum and its posts

    :param request: HTTP request to HTML template
    :return: Jinja template with request and posts data
    """

    return templates.TemplateResponse(
        "homepage.html",
        {
            "request": request,
            "posts": sorted(
                [Post.get(k) for k in Post.all_pks()],
                key=lambda x: x.updated_at,
                reverse=True
            )
        }
    )


@router.get("/post/{pk}")
def view_post(request: Request, pk: str):
    """ View post and replies

    Path is defined in html template, where the view link sends to
    /post/{pk}

    :param request: HTTP request to HTML template
    :param pk: post id generated by redis-om
    :return: Jinja template with request and selected post data with replies
    """

    print("Current post:", pk)

    post = Post.get(pk)

    return templates.TemplateResponse(
        "viewpage.html",
        {
            "request": request,
            "title": post.title,
            "content": post.content,
            "replies": list(
                sorted(
                    filter(lambda x: x.post_id == pk, [Reply.get(k) for k in Reply.all_pks()]),
                    key=lambda x: x.created_at,
                    reverse=False
                )
            )
        }
    )


@router.post("/post", status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    """ Create post with POST request

    :param post: object via POST request
    :return: save post 
    """

    print("Post created:", post)

    return post.save()


# == FOR TESTING AND CLEAN-UP ==================================================

@router.get("/post", status_code=status.HTTP_200_OK)
def view_posts():

    return [Post.get(k) for k in Post.all_pks()]


@router.delete("/post", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_post():

    [Post.delete(pk) for pk in Post.all_pks()]

    return Response(content="All posts deleted.")
