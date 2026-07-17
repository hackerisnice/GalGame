# 角色定义
define narrator = Character(None, what_italic=True)
define brother = Character("[brother_name]", color="#66ccff")
define me = Character("[myname]", color="#ff9966")

# 音频预留（放入后删除 # 号即可）
# define audio.bgm_school = "audio/bgm_school.mp3"
# define audio.bgm_tense = "audio/bgm_tense.mp3"

# 变量
default myname = ""
default brother_name = "小翔"
default affection = 50        # 好感度 0-100
default day = 1

# 好感度显示条（右上角）
screen affection_hud():
    frame:
        xalign 0.98 yalign 0.02
        xsize 260 ysize 60
        background "#000000aa"
        padding (10, 10)
        vbox:
            text "好感度" size 16 color "#ffffff"
            bar value affection range 100 xsize 220 ysize 12
            text "[affection] / 100" size 14 color "#cccccc" xalign 0.5

# 开始
label start:
    scene bg_black
    "请输入你的名字："
    $ myname = renpy.input("我叫……", default="小明", length=12)
    $ myname = myname.strip()
    if myname == "":
        $ myname = "PLAYER"
    "你的名字是 [myname]。"
    show screen affection_hud
    jump chapter1

label chapter1:
    scene bg_school_gate
    # play music bgm_school fadein 1.0
    "九月，阳光穿过校门的梧桐叶。"
    "我和[brother_name]从小一起长大，今天是高中开学第一天。"
    show brother normal at left
    brother "喂，[myname]，作业借我抄抄！"
    me "又来了……哪次不是我给你补。"
    brother "嘿嘿，兄弟嘛！"
    "直到那天晚上……"
    scene bg_room_night
    # stop music fadeout 1.0
    # play music bgm_tense fadein 1.0
    "半夜，我被隔壁的动静吵醒。"
    "推开房门，床上坐着一个陌生女孩。"
    show brother surprised at center
    $ brother.name = "???"
    brother "别、别过来！"
    me "你谁啊？！[brother_name]呢？"
    brother "我就是[brother_name]……"
    $ brother.name = brother_name
    brother "我们七岁那年偷西瓜的事，只有我俩知道。"
    menu:
        "冷静下来，先听他/她说清楚":
            $ affection += 10
            me "好吧，我相信你。别慌，慢慢说。"
            brother "谢谢你，[myname]……"
        "这一定是梦，我回去睡觉":
            $ affection -= 5
            me "我一定是没睡醒……再见。"
            brother "喂！不准走！"
            "一只纤细的手死死拽住我衣角。"
    if affection >= 60:
        brother "你果然是我最好的朋友。"
    else:
        brother "算了……我知道很难接受。"
    "花了整整一个小时，我才接受：我的兄弟变成了女孩子。"
    jump chapter2

label chapter2:
    scene bg_classroom
    # play music bgm_school fadein 1.0
    "第二天，[brother_name]穿着我的旧校服来上课，还成了我的同桌。"
    show brother shy at right
    brother "[myname]，笔记借我看看。"
    me "你以前不是最讨厌笔记吗？"
    brother "现在……想认真一点。"
    menu:
        "向大家解释：这是我表妹":
            $ affection += 5
            me "这是我表妹，今天刚转来。"
            brother "（小声）你占我便宜……"
        "什么都不说，让他们猜":
            me "（沉默）"
            "同桌的八卦之火越烧越旺。"
    if affection >= 70:
        brother "不过……和你当同桌，好像也没那么糟。"
    elif affection < 30:
        brother "总觉得你一直在躲我。"
    "午休时，[brother_name]趴在桌上睡着了。"
    menu:
        "帮她披上外套":
            $ affection += 10
            "我轻轻把外套搭在她身上。"
            brother "（梦话）[myname]……"
        "偷偷戳一下脸":
            $ affection += 5
            "好软。完了，我在干什么。"
            brother "嗯……？"
    "我莫名有种预感：我和[brother_name]的关系，再也回不去了。"
    "（未完待续）"
    return
