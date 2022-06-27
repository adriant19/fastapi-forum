from fastapi import APIRouter, Request, status, Response
from fastapi.templating import Jinja2Templates
from app.schemas import Post, Reply
from datetime import datetime


router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


# -- Requests ------------------------------------------------------------------

@router.post("/reply", status_code=status.HTTP_201_CREATED)
def create_reply(reply: Reply):
    """ Create reply with POST request

    :param reply: object via POST request
    :return: save reply under post id
    """

    post = Post.get(reply.post_id)

    post.replies += 1
    post.updated_at = datetime.now()

    post.save()

    print("Reply created:", reply)

    return reply.save()


# == FOR TESTING AND CLEAN-UP ==================================================

@router.delete("/reply", status_code=status.HTTP_204_NO_CONTENT)
def delete_all_reply():

    [Reply.delete(pk) for pk in Reply.all_pks()]

    return Response(content="All posts deleted.")


@router.get("/reply", status_code=status.HTTP_200_OK)
def view_replies():

    return [Reply.get(k) for k in Reply.all_pks()]
