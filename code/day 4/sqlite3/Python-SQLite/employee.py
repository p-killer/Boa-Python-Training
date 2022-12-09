#schema
class Employee:
    """A sample Employee class"""

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

  


''' table->model->DTO-> JSON serialized by flaskREST/Django REST


DAL (models, DTO, context (CRUD)
BAL ( modules for BL , Third pary rest calls)
PAL  (flask UI (html + css + python + javascript (D3.js)))
Extensions/ utilities ( Decoraters, generarators.)
IAL : security (JWT), Logging,caching) - Cross cutting concerns, asyncio (scalable Load balancer)
main.py
'''