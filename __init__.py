from hoshino.service import Service
import hoshino

sv = Service('吃饭啦', enable_on_default=False,
             use_priv=hoshino.priv.PRIVATE, help_='每天定时提醒点外卖')
logger = sv.logger


@sv.scheduled_job('cron', hour='10,16', minute="40")
async def call_ff_eat():
    user_ids = hoshino.config.feifood.USERS
    if user_ids is None:
        return
    for user_id in user_ids:
        logger.debug(f"正在给{user_id}发送吃饭提醒")
        await sv.bot.send_private_msg(user_id, "该点外卖啦")
