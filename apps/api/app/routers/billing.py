from fastapi import APIRouter

router = APIRouter(prefix="/billing", tags=["billing"])

@router.post("/webhook/stripe")
async def stripe_webhook():
    return {"status": "ok"}

@router.post("/webhook/razorpay")
async def razorpay_webhook():
    return {"status": "ok"}
