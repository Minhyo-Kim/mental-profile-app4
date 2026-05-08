"""규칙 기반 총평 생성기 - 김선우 총평 스타일 기준"""

# ── 수준 판단 함수 ─────────────────────────────────────────────────────────────

def level_30(val):
    """30점 만점 기준 수준"""
    if val >= 23: return "high"
    elif val >= 15: return "mid"
    else: return "low"

def level_sc(val):
    """스포츠자신감 5점 만점 (높을수록 좋음)"""
    if val >= 4.8: return "perfect"    # 만점/매우 이상적
    elif val >= 4.0: return "high"     # 높음
    elif val >= 3.0: return "mid"      # 보통
    else: return "low"                 # 낮음

def level_pos(val):
    """수행전략 긍정 (높을수록 좋음)"""
    if val >= 4.8: return "perfect"
    elif val >= 4.0: return "high"
    elif val >= 3.0: return "mid"
    else: return "low"

def level_neg(val):
    """수행전략 부정 (낮을수록 좋음)"""
    if val <= 1.5: return "perfect"    # 이상적
    elif val <= 2.5: return "good"     # 양호
    elif val <= 3.5: return "fair"     # 다소 높음
    else: return "high"                # 높음


# ── 단락 생성 함수 ────────────────────────────────────────────────────────────

def para1_overall_optimism(data):
    """①전반 총평 + 낙관성"""
    name = data['name']
    opt = data['optimism']
    opt_lv = level_30(opt)

    # 전반 인상 결정 (불안/자신감 종합)
    ta = data['trait_anxiety']
    ca = data['cognitive_anxiety']
    sa = data['somatic_anxiety']
    sc = data['state_confidence']
    avg_anxiety = (ca + sa) / 2
    
    if avg_anxiety <= 13 and sc >= 20 and ta <= 17:
        overall = "전반적으로 심리적으로 매우 안정되고 준비된 상태임을 보여주고 있습니다."
    elif avg_anxiety <= 17 and sc >= 17:
        overall = "전반적으로 심리적 준비 상태가 양호한 편으로 나타났습니다."
    elif avg_anxiety >= 20 or sc <= 14:
        overall = "전반적으로 시합 상황에서 심리적 부담과 긴장을 크게 느끼는 편으로 나타났습니다."
    else:
        overall = "전반적으로 일부 영역에서 심리적 지원이 필요한 것으로 나타났습니다."

    # 낙관성 표현
    opt_texts = {
        "high": "낙관성이 높게 나타나 어려운 상황에서도 긍정적으로 해석하고 회복하는 심리적 자원이 잘 갖춰져 있습니다.",
        "mid": "낙관성은 중간 수준으로 나타나 어려운 상황에서도 긍정적인 방향으로 해석하려는 기본적인 경향이 갖춰져 있습니다.",
        "low": "낙관성이 다소 낮게 나타나 어려운 상황에서 부정적으로 해석하거나 위축될 가능성이 있어 주의가 필요합니다.",
    }
    return f"{name} 선수의 스포츠심리측정 결과, {overall} {opt_texts[opt_lv]}"


def para2_anxiety(data):
    """②특성불안 + 상태불안"""
    ta_lv = level_30(data['trait_anxiety'])
    ca_lv = level_30(data['cognitive_anxiety'])
    sa_lv = level_30(data['somatic_anxiety'])
    sc_lv = level_30(data['state_confidence'])

    # 특성불안
    ta_texts = {
        "high": "스포츠경쟁불안(특성불안)이 높게 나타나, 중요한 경기일수록 압박감이 크게 작용하거나 경기 전부터 부담을 많이 느낄 수 있습니다.",
        "mid": "스포츠경쟁불안(특성불안)은 중간 수준으로, 중요한 경기에서 일정한 긴장이나 부담을 느낄 수 있으나 수행을 방해할 정도로 크지는 않은 편입니다.",
        "low": "스포츠경쟁불안(특성불안)이 낮게 나타나, 경쟁 상황에서도 비교적 안정적으로 심리 상태를 유지하는 편입니다.",
    }

    # 인지/신체불안 조합
    if ca_lv == "low" and sa_lv == "low":
        anx_text = "상태불안 결과에서는 인지적 불안과 신체적 불안 모두 낮게 나타났습니다."
    elif ca_lv == "high" and sa_lv == "high":
        anx_text = "상태불안 결과에서는 인지적 불안과 신체적 불안 모두 높게 나타나, 경기 전후로 생각이 많아지고 몸의 긴장도 함께 올라오는 형태가 나타날 수 있습니다."
    elif ca_lv == "high":
        anx_text = "상태불안 결과에서는 인지적 불안이 높게 나타나 경기 전후로 생각이 많아지거나 걱정이 커지는 형태가 나타날 수 있으며, 신체적 불안은 비교적 양호한 수준입니다."
    elif sa_lv == "high":
        anx_text = "상태불안 결과에서는 신체적 불안이 높게 나타나 몸의 긴장이 심하게 올라올 수 있으며, 인지적 불안은 비교적 양호한 수준입니다."
    else:
        anx_text = "상태불안 결과에서는 인지적 불안과 신체적 불안 모두 중간 수준으로 나타났습니다."

    # 상태자신감
    sc_texts = {
        "high": "상태 자신감이 높게 나타나 경기 상황에서 자기 확신이 강점으로 작용할 수 있습니다.",
        "mid": "상태 자신감은 중간 수준으로 나타났습니다.",
        "low": "상태 자신감이 낮게 나타나, 긴장 상황에서 '할 수 있다'는 마음을 유지하는 것이 쉽지 않을 수 있습니다.",
    }

    return f"{ta_texts[ta_lv]} {anx_text} {sc_texts[sc_lv]}"


def para3_sport_confidence(data):
    """③스포츠 자신감"""
    scores = {
        '능력입증': data['sc_ability'],
        '코치 지도력': data['sc_coach'],
        '사회적 지지': data['sc_social'],
        '신체·정신적 준비': data['sc_physical'],
    }
    levels = {k: level_sc(v) for k, v in scores.items()}

    perfect = [k for k, lv in levels.items() if lv == "perfect"]
    high = [k for k, lv in levels.items() if lv == "high"]
    mid = [k for k, lv in levels.items() if lv == "mid"]
    low = [k for k, lv in levels.items() if lv == "low"]

    # 모두 만점
    if len(perfect) == 4:
        return ("스포츠 자신감(자신감의 원천)에서는 능력입증, 코치 지도력, 사회적 지지, 신체·정신적 준비 요인이 모두 만점으로 나타났습니다. "
                "이는 훈련 과정에서의 준비감과 코치에 대한 신뢰, 주변의 응원 등 자신감을 구성하는 모든 요소가 매우 탄탄하게 갖춰져 있음을 의미합니다.")

    # 모두 높음 이상
    if len(perfect) + len(high) == 4:
        names = list(scores.keys())
        return (f"스포츠 자신감(자신감의 원천)에서는 {', '.join(names)} 요인 모두 높게 나타났습니다. "
                "자신감을 구성하는 전반적인 요소들이 잘 갖춰져 있어 경기 상황에서 안정적인 자신감을 발휘할 수 있을 것입니다.")

    # 강점/약점 혼합
    good = perfect + high
    weak = low + mid

    if good and weak:
        good_str = ', '.join(good)
        weak_str = ', '.join(weak)
        return (f"스포츠 자신감(자신감의 원천)에서는 {good_str} 요인이 높게 나타난 반면, "
                f"{weak_str}이(가) 다소 낮게 나타났습니다. "
                f"{weak_str} 측면에서의 자신감이 충분히 형성될 수 있도록 지속적인 관심이 필요합니다.")
    elif not weak:
        return ("스포츠 자신감(자신감의 원천)에서는 전반적으로 양호한 수준으로 나타났습니다. "
                "자신감의 다양한 원천이 고루 갖춰져 있어 경기 상황에서 안정적인 자신감을 유지할 수 있을 것입니다.")
    else:
        weak_str = ', '.join(weak)
        return (f"스포츠 자신감(자신감의 원천)에서는 전반적으로 발달이 필요한 것으로 나타났습니다. "
                f"특히 {weak_str} 측면의 자신감을 높이기 위한 체계적인 지원이 필요합니다.")


def para4_performance_strategy(data):
    """④수행전략 + 실천 제언"""
    pos = {
        '혼잣말': data['ps_self_talk'],
        '자동적수행': data['ps_auto'],
        '심상': data['ps_imagery'],
        '긴장풀기': data['ps_relax'],
        '목표설정': data['ps_goal'],
    }
    neg = {
        '부정적 생각': data['ps_negative'],
        '주의산만': data['ps_distract'],
        '감정조절': data['ps_emotion'],
    }

    pos_levels = {k: level_pos(v) for k, v in pos.items()}
    neg_levels = {k: level_neg(v) for k, v in neg.items()}

    # 긍정 전략 분류
    pos_ideal = [k for k, lv in pos_levels.items() if lv in ("perfect", "high")]
    pos_weak = [k for k, lv in pos_levels.items() if lv in ("mid", "low")]

    # 부정 전략 분류
    neg_ideal = [k for k, lv in neg_levels.items() if lv in ("perfect", "good")]
    neg_concern = [k for k, lv in neg_levels.items() if lv in ("fair", "high")]

    parts = []

    # 긍정 전략 표현
    if len(pos_ideal) >= 4:
        parts.append(f"수행전략에서는 {', '.join(pos_ideal)} 전략이 이상적인 수준에 가깝게 잘 활용되고 있습니다.")
    elif pos_ideal:
        parts.append(f"수행전략에서는 {', '.join(pos_ideal)}이(가) 비교적 잘 활용되고 있습니다.")
    else:
        parts.append("수행전략 전반에서 추가적인 발달이 필요한 것으로 나타났습니다.")

    if pos_weak:
        parts.append(f"{', '.join(pos_weak)}은(는) 이상적인 수준에 비해 다소 부족하게 나타났습니다.")

    # 부정 전략 + 실천 제언
    if neg_concern:
        concern_str = ', '.join(neg_concern)
        if '부정적 생각' in neg_concern and '주의산만' in neg_concern:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 다소 높게 나타나, "
                      "경기 흐름이 꼬이거나 실수가 발생하는 상황에서 집중력이 흔들리거나 부정적인 생각이 유입될 수 있습니다. "
                      "실수 후 빠르게 현재에 집중하는 루틴을 훈련 과정에서 꾸준히 연습한다면 경기 운영에 도움이 될 것입니다.")
        elif '부정적 생각' in neg_concern:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 높게 나타나, "
                      "경기 중 부정적인 생각이 수행에 영향을 줄 수 있습니다. "
                      "부정적인 생각을 인식하고 전환하는 심리기술 훈련을 체계적으로 익혀나가길 권장합니다.")
        elif '주의산만' in neg_concern:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 높게 나타나, "
                      "경기 상황에서 집중력이 흔들릴 수 있습니다. "
                      "루틴 개발과 주의 집중 훈련을 통해 집중력을 강화하는 것을 권장합니다.")
        else:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 높게 나타났습니다. "
                      "스포츠심리상담을 통해 개인에게 맞는 심리기술을 체계적으로 익혀나가길 권장합니다.")
        parts.append(advice)
    else:
        parts.append("부정적 생각과 주의산만도 이상적인 수준으로 잘 관리되고 있어, "
                     "지속적인 심리기술 훈련을 통해 현재의 강점을 더욱 공고히 하는 것을 권장합니다.")

    return " ".join(parts)


def generate_commentary(data):
    """4단락 총평 생성 (줄바꿈으로 구분)"""
    p1 = para1_overall_optimism(data)
    p2 = para2_anxiety(data)
    p3 = para3_sport_confidence(data)
    p4 = para4_performance_strategy(data)
    return f"{p1}\n{p2}\n{p3}\n{p4}"


# ── 테스트 ────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    test_data = {
        'name': '김선우', 'sport': '레슬링',
        'optimism': 19, 'trait_anxiety': 17,
        'cognitive_anxiety': 13, 'somatic_anxiety': 10, 'state_confidence': 22,
        'sc_ability': 5.0, 'sc_social': 5.0, 'sc_coach': 5.0, 'sc_physical': 5.0,
        'ps_self_talk': 4.5, 'ps_auto': 5.0, 'ps_imagery': 5.0, 'ps_relax': 5.0,
        'ps_goal': 5.0, 'ps_emotion': 1.25, 'ps_negative': 2.5, 'ps_distract': 2.0,
    }
    print(generate_commentary(test_data))

"""선수 심리측정 결과 PPT 자동 생성기"""
import sys, os, re, shutil, zipfile
import pandas as pd
from datetime import datetime
from io import BytesIO

FIXED_RPR = '<a:rPr lang="ko-KR" altLang="ko-KR" sz="1200" dirty="0"><a:solidFill><a:schemeClr val="tx1"/></a:solidFill><a:latin typeface="한컴산뜻돋움" panose="02000000000000000000" pitchFamily="2" charset="-127"/><a:ea typeface="한컴산뜻돋움" panose="02000000000000000000" pitchFamily="2" charset="-127"/></a:rPr>'
FIXED_PPR = '<a:pPr algn="just"><a:lnSpc><a:spcPct val="150000"/></a:lnSpc></a:pPr>'

def replace_nth(text, pattern, replacement, n):
    matches = list(re.finditer(pattern, text))
    if len(matches) < n: return text
    m = matches[n-1]
    return text[:m.start()] + replacement + text[m.end():]

def xesc(t):
    return t.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('"','&quot;')

def make_para(text):
    return f'<a:p>{FIXED_PPR}<a:r>{FIXED_RPR}<a:t xml:space="preserve">{xesc(text)}</a:t></a:r></a:p>'

# ── 데이터 로드 ────────────────────────────────────────────────────────────────

def load_athlete_data(excel_input, athlete_name):
    """excel_input: 파일경로(str) 또는 DataFrame"""
    if isinstance(excel_input, pd.DataFrame):
        df = excel_input
    else:
        df = pd.read_excel(excel_input, sheet_name='개인측정코딩')

    row = df[df['성명'] == athlete_name]
    if row.empty:
        names = df['성명'].dropna().tolist()
        raise ValueError(f"'{athlete_name}' 없음.\n등록된 선수: {', '.join(names)}")
    row = row.iloc[0]

    dob = str(int(row['생년월일(예: 070801)'])).zfill(6)
    y, m, d = int(dob[:2]), int(dob[2:4]), int(dob[4:6])
    yr = 2000+y if y<=30 else 1900+y
    today = datetime.today()

    return {
        'name': athlete_name,
        'sport': str(row['종목']).strip(),
        'dob_year': yr, 'dob_month': m, 'dob_day': d,
        'measure_year': today.year, 'measure_month': today.month, 'measure_day': today.day,

        # 경쟁상태불안 (30점 환산)
        'cognitive_anxiety': round(float(row['환_인지불안'])),
        'somatic_anxiety':   round(float(row['환_신체불안'])),
        'state_confidence':  round(float(row['환_자신감'])),

        # 낙관성/특성불안 (텍스트만)
        'trait_anxiety': int(row['스포츠경쟁불안(합)']),
        'optimism':      int(row['낙관성(합)']),

        # 스포츠 자신감 (5점 만점, 높을수록 좋음)
        'sc_ability':  float(row['능력입증(평)']),
        'sc_social':   float(row['사회적지지(평)']),
        'sc_coach':    float(row['코치지도력(평)']),
        'sc_physical': float(row['신체적/정신적 준비(평)']),

        # 수행전략 (5점 만점)
        # 긍정: 높을수록 좋음
        'ps_self_talk': float(row['혼잣말(평)']),
        'ps_auto':      float(row['자동적수행(평)']),
        'ps_imagery':   float(row['심상(평)']),
        'ps_relax':     float(row['긴장풀기(평)']),
        'ps_goal':      float(row['목표설정(평)']),
        # 부정: 낮을수록 좋음
        'ps_emotion':   float(row['감정조절(평)']),
        'ps_negative':  float(row['부정적생각(평)']),
        'ps_distract':  float(row['주의산만(평)']),
    }

# ── 슬라이드 수정 ─────────────────────────────────────────────────────────────

def update_slide1(path, data):
    with open(path,'r',encoding='utf-8') as f: c=f.read()
    n=data['name']; sp=f"{n[0]} {n[1]} {n[2]}" if len(n)==3 else n
    c=c.replace('>김 도 담<',f'>{sp}<')
    c=c.replace('>레슬링<',f'>{data["sport"]}<')
    dy,dm,dd = data['dob_year'],data['dob_month'],data['dob_day']
    my,mm,md = data['measure_year'],data['measure_month'],data['measure_day']
    i1=c.find('>2009<'); e1=c.find('>일<',i1)+5
    b1=c[i1:e1]
    b1=b1.replace('>2009<',f'>{dy}<',1)
    b1=replace_nth(b1,r'> \d\d<',f'> {dm:02d}<',1)
    b1=replace_nth(b1,r'> \d\d<',f'> {dd:02d}<',2)
    c=c[:i1]+b1+c[e1:]
    i2=c.find('>2026<'); e2=c.find('>일<',i2)+5
    b2=c[i2:e2]
    b2=b2.replace('>2026<',f'>{my}<',1)
    b2=replace_nth(b2,r'> \d\d<',f'> {mm:02d}<',1)
    b2=replace_nth(b2,r'> \d\d<',f'> {md:02d}<',2)
    c=c[:i2]+b2+c[e2:]
    with open(path,'w',encoding='utf-8') as f: f.write(c)

def update_slide2_text(path, data):
    """슬라이드2 텍스트: 낙관성/특성불안/경쟁상태불안 숫자"""
    with open(path,'r',encoding='utf-8') as f: c=f.read()
    # 인지불안/신체불안/자신감 (30점 환산) - 도넛 옆 숫자
    for old,new in [('>24<',f'>{data["cognitive_anxiety"]}<'),
                    ('>20<',f'>{data["somatic_anxiety"]}<'),
                    ('>16<',f'>{data["state_confidence"]}<'),
                    # 특성불안 괄호값
                    ('>17<',f'>{data["trait_anxiety"]}<'),
                    ('>25<',f'>{data["optimism"]}<'),
                    # 아래 큰 숫자
                    ('>17<',f'>{data["trait_anxiety"]}<'),
                    ('>25<',f'>{data["optimism"]}<')]:
        c=c.replace(old,new,1)
    with open(path,'w',encoding='utf-8') as f: f.write(c)

def update_donut_chart(path, value, max_val=30):
    """도넛 차트: [실제값, 0, 나머지] 구조"""
    with open(path,'r',encoding='utf-8') as f: c=f.read()
    remainder = max_val - value
    # idx=0: 실제값, idx=1: 0(간격), idx=2: 나머지
    def replace_pt(xml, idx, new_val):
        pattern = f'<c:pt idx="{idx}">\\s*<c:v>[^<]*</c:v>'
        replacement = f'<c:pt idx="{idx}"><c:v>{new_val}</c:v>'
        return re.sub(pattern, replacement, xml)
    c = replace_pt(c, 0, value)
    c = replace_pt(c, 1, 0)
    c = replace_pt(c, 2, remainder)
    with open(path,'w',encoding='utf-8') as f: f.write(c)

def update_bar_chart(path, ability, social, coach, physical):
    """스포츠자신감 막대그래프 (chart7): 4개 값 교체"""
    with open(path,'r',encoding='utf-8') as f: c=f.read()
    values = [ability, social, coach, physical]
    # 기존 값: 4.5, 3.7, 3, 4.5 순서로 교체
    old_vals = [r'<c:v>4\.5</c:v>', r'<c:v>3\.7</c:v>', r'<c:v>3</c:v>', r'<c:v>4\.5</c:v>']
    for old, new_v in zip(old_vals, values):
        c = re.sub(old, f'<c:v>{round(new_v,4)}</c:v>', c, count=1)
    with open(path,'w',encoding='utf-8') as f: f.write(c)

def update_radar_chart(path, self_talk, auto, imagery, relax, goal, emotion, negative, distract):
    """수행전략 레이더 차트 (chart8): 검사결과 8개 값 교체"""
    with open(path,'r',encoding='utf-8') as f: c=f.read()
    new_vals = [self_talk, auto, imagery, relax, goal, emotion, negative, distract]
    # 기존 검사결과 값 (이상적결과 5,5,5,5,5,1,1,1 다음에 나오는 8개)
    old_vals = [
        r'<c:v>3</c:v>',
        r'<c:v>2\.3333333333333335</c:v>',
        r'<c:v>4</c:v>',
        r'<c:v>2\.75</c:v>',
        r'<c:v>4</c:v>',
        r'<c:v>1\.75</c:v>',
        r'<c:v>5</c:v>',
        r'<c:v>3\.3333333333333335</c:v>',
    ]
    for old, new_v in zip(old_vals, new_vals):
        c = re.sub(old, f'<c:v>{round(new_v,4)}</c:v>', c, count=1)
    with open(path,'w',encoding='utf-8') as f: f.write(c)

def replace_para(c, anchor, new_text):
    idx=c.find(anchor)
    if idx==-1: return c
    ps=c.rfind('<a:p>',0,idx); pe=c.find('</a:p>',idx)+len('</a:p>')
    return c[:ps]+make_para(new_text)+c[pe:]

def update_slide3(path, data, commentary=None):
    with open(path,'r',encoding='utf-8') as f: c=f.read()

    if not commentary:
        # 이름만 교체
        c = c.replace('>김도담<', f'>{data["name"]}<')
        with open(path,'w',encoding='utf-8') as f: f.write(c)
        return

    # 총평 단락 분리
    paras = [p.strip() for p in commentary.strip().split('\n') if p.strip()]

    # 총평 텍스트박스 찾기 (김도담이 포함된 txBody)
    idx = c.find('>김도담<')
    if idx == -1:
        # 이미 이름이 바뀐 경우
        idx = c.find(f'>{data["name"]}<')
    txbody_start = c.rfind('<p:txBody>', 0, idx)
    txbody_end = c.find('</p:txBody>', idx) + len('</p:txBody>')
    txbody_old = c[txbody_start:txbody_end]

    # 기존 단락에서 pPr, rPr 추출 (폰트 보존)
    ppr_m = re.search(r'<a:pPr.*?</a:pPr>', txbody_old, re.DOTALL)
    rpr_m = re.search(r'<a:rPr lang="ko-KR".*?</a:rPr>', txbody_old, re.DOTALL)
    ppr = ppr_m.group(0) if ppr_m else FIXED_PPR
    rpr = rpr_m.group(0) if rpr_m else FIXED_RPR

    def make_para_with_style(text):
        escaped = xesc(text)
        return f'<a:p>{ppr}<a:r>{rpr}<a:t xml:space="preserve">{escaped}</a:t></a:r></a:p>'

    # 새 단락들 생성 (총평 4단락)
    new_paras = ''.join(make_para_with_style(p) for p in paras)

    # txBody 내부의 모든 <a:p> 블록을 새 단락으로 교체
    # txBody 헤더(bodyPr 등) 보존
    txbody_header_end = txbody_old.find('<a:p>')
    txbody_footer_start = txbody_old.rfind('</a:p>') + len('</a:p>')
    txbody_new = (txbody_old[:txbody_header_end] +
                  new_paras +
                  txbody_old[txbody_footer_start:])

    c = c[:txbody_start] + txbody_new + c[txbody_end:]
    with open(path,'w',encoding='utf-8') as f: f.write(c)

# ── 메인 생성 함수 ────────────────────────────────────────────────────────────

def generate_ppt_bytes(pptx_bytes, data):
    """pptx_bytes를 받아 수정된 pptx bytes 반환 (Streamlit용)"""
    import tempfile
    work_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(BytesIO(pptx_bytes)) as z:
            z.extractall(work_dir)
        _apply_data(work_dir, data)
        buf = BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(work_dir):
                for file in files:
                    fp = os.path.join(root, file)
                    z.write(fp, os.path.relpath(fp, work_dir))
        buf.seek(0)
        return buf.read()
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

def generate_ppt(excel_path, template_path, athlete_name, output_dir="."):
    """파일 경로로 직접 실행 (CLI용)"""
    data = load_athlete_data(excel_path, athlete_name)
    print(f"✅ {data['name']} | {data['sport']} | {data['dob_year']}년 {data['dob_month']:02d}월 {data['dob_day']:02d}일")

    work_dir = f"/tmp/ppt_{athlete_name}"
    if os.path.exists(work_dir): shutil.rmtree(work_dir)
    os.system(f"python /mnt/skills/public/pptx/scripts/office/unpack.py '{template_path}' '{work_dir}' 2>/dev/null")
    _apply_data(work_dir, data)
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    sport_safe = re.sub(r'[,/ ]','_', data['sport']).strip('_')
    out = os.path.join(output_dir, f"{today}_{sport_safe}_{athlete_name}_멘탈프로파일.pptx")
    os.system(f"python /mnt/skills/public/pptx/scripts/office/pack.py '{work_dir}' '{out}' --original '{template_path}' 2>/dev/null")
    shutil.rmtree(work_dir)
    print(f"✨ 완료 → {out}")
    return out, data

def _apply_data(work_dir, data):
    """실제 데이터 적용 (공통)"""
    slides = os.path.join(work_dir, "ppt", "slides")
    charts = os.path.join(work_dir, "ppt", "charts")

    # 슬라이드1: 기본 정보
    update_slide1(os.path.join(slides, "slide1.xml"), data)

    # 슬라이드2: 텍스트 숫자
    update_slide2_text(os.path.join(slides, "slide2.xml"), data)

    # 도넛 차트 (경쟁상태불안 3개)
    update_donut_chart(os.path.join(charts, "chart4.xml"), data['cognitive_anxiety'])   # 인지불안
    update_donut_chart(os.path.join(charts, "chart5.xml"), data['state_confidence'])    # 상태자신감
    update_donut_chart(os.path.join(charts, "chart6.xml"), data['somatic_anxiety'])     # 신체불안

    # 스포츠자신감 막대그래프
    update_bar_chart(
        os.path.join(charts, "chart7.xml"),
        data['sc_ability'], data['sc_social'], data['sc_coach'], data['sc_physical']
    )

    # 수행전략 레이더 차트
    update_radar_chart(
        os.path.join(charts, "chart8.xml"),
        data['ps_self_talk'], data['ps_auto'], data['ps_imagery'], data['ps_relax'],
        data['ps_goal'], data['ps_emotion'], data['ps_negative'], data['ps_distract']
    )

    # 슬라이드3: 규칙 기반 총평 생성 후 삽입
    commentary = data.get('commentary') or generate_commentary(data)
    update_slide3(os.path.join(slides, "slide3.xml"), data, commentary)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("사용법: python generate_ppt.py [엑셀] [PPT템플릿] [선수명] [출력폴더]")
        sys.exit(1)
    generate_ppt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv)>4 else ".")



"""규칙 기반 총평 생성기 - 김선우 총평 스타일 기준"""


# ── 메인 생성 함수 ────────────────────────────────────────────────────────────

def generate_ppt_bytes(pptx_bytes, data):
    """pptx_bytes를 받아 수정된 pptx bytes 반환 (Streamlit용)"""
    import tempfile
    work_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(BytesIO(pptx_bytes)) as z:
            z.extractall(work_dir)
        _apply_data(work_dir, data)
        buf = BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(work_dir):
                for file in files:
                    fp = os.path.join(root, file)
                    z.write(fp, os.path.relpath(fp, work_dir))
        buf.seek(0)
        return buf.read()
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

def generate_ppt(excel_path, template_path, athlete_name, output_dir="."):
    """파일 경로로 직접 실행 (CLI용)"""
    data = load_athlete_data(excel_path, athlete_name)
    print(f"✅ {data['name']} | {data['sport']} | {data['dob_year']}년 {data['dob_month']:02d}월 {data['dob_day']:02d}일")

    work_dir = f"/tmp/ppt_{athlete_name}"
    if os.path.exists(work_dir): shutil.rmtree(work_dir)
    os.system(f"python /mnt/skills/public/pptx/scripts/office/unpack.py '{template_path}' '{work_dir}' 2>/dev/null")
    _apply_data(work_dir, data)
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    sport_safe = re.sub(r'[,/ ]','_', data['sport']).strip('_')
    out = os.path.join(output_dir, f"{today}_{sport_safe}_{athlete_name}_멘탈프로파일.pptx")
    os.system(f"python /mnt/skills/public/pptx/scripts/office/pack.py '{work_dir}' '{out}' --original '{template_path}' 2>/dev/null")
    shutil.rmtree(work_dir)
    print(f"✨ 완료 → {out}")
    return out, data

def _apply_data(work_dir, data):
    """실제 데이터 적용 (공통)"""
    slides = os.path.join(work_dir, "ppt", "slides")
    charts = os.path.join(work_dir, "ppt", "charts")

    # 슬라이드1: 기본 정보
    update_slide1(os.path.join(slides, "slide1.xml"), data)

    # 슬라이드2: 텍스트 숫자
    update_slide2_text(os.path.join(slides, "slide2.xml"), data)

    # 도넛 차트 (경쟁상태불안 3개)
    update_donut_chart(os.path.join(charts, "chart4.xml"), data['cognitive_anxiety'])   # 인지불안
    update_donut_chart(os.path.join(charts, "chart5.xml"), data['state_confidence'])    # 상태자신감
    update_donut_chart(os.path.join(charts, "chart6.xml"), data['somatic_anxiety'])     # 신체불안

    # 스포츠자신감 막대그래프
    update_bar_chart(
        os.path.join(charts, "chart7.xml"),
        data['sc_ability'], data['sc_social'], data['sc_coach'], data['sc_physical']
    )

    # 수행전략 레이더 차트
    update_radar_chart(
        os.path.join(charts, "chart8.xml"),
        data['ps_self_talk'], data['ps_auto'], data['ps_imagery'], data['ps_relax'],
        data['ps_goal'], data['ps_emotion'], data['ps_negative'], data['ps_distract']
    )

    # 슬라이드3: 규칙 기반 총평 생성 후 삽입
    commentary = data.get('commentary') or generate_commentary(data)
    update_slide3(os.path.join(slides, "slide3.xml"), data, commentary)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("사용법: python generate_ppt.py [엑셀] [PPT템플릿] [선수명] [출력폴더]")
        sys.exit(1)
    generate_ppt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv)>4 else ".")



"""규칙 기반 총평 생성기 - 김선우 총평 스타일 기준"""

# ── 메인 생성 함수 ────────────────────────────────────────────────────────────

def generate_ppt_bytes(pptx_bytes, data):
    """pptx_bytes를 받아 수정된 pptx bytes 반환 (Streamlit용)"""
    import tempfile
    work_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(BytesIO(pptx_bytes)) as z:
            z.extractall(work_dir)
        _apply_data(work_dir, data)
        buf = BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(work_dir):
                for file in files:
                    fp = os.path.join(root, file)
                    z.write(fp, os.path.relpath(fp, work_dir))
        buf.seek(0)
        return buf.read()
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

def generate_ppt(excel_path, template_path, athlete_name, output_dir="."):
    """파일 경로로 직접 실행 (CLI용)"""
    data = load_athlete_data(excel_path, athlete_name)
    print(f"✅ {data['name']} | {data['sport']} | {data['dob_year']}년 {data['dob_month']:02d}월 {data['dob_day']:02d}일")

    work_dir = f"/tmp/ppt_{athlete_name}"
    if os.path.exists(work_dir): shutil.rmtree(work_dir)
    os.system(f"python /mnt/skills/public/pptx/scripts/office/unpack.py '{template_path}' '{work_dir}' 2>/dev/null")
    _apply_data(work_dir, data)
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    sport_safe = re.sub(r'[,/ ]','_', data['sport']).strip('_')
    out = os.path.join(output_dir, f"{today}_{sport_safe}_{athlete_name}_멘탈프로파일.pptx")
    os.system(f"python /mnt/skills/public/pptx/scripts/office/pack.py '{work_dir}' '{out}' --original '{template_path}' 2>/dev/null")
    shutil.rmtree(work_dir)
    print(f"✨ 완료 → {out}")
    return out, data

def _apply_data(work_dir, data):
    """실제 데이터 적용 (공통)"""
    slides = os.path.join(work_dir, "ppt", "slides")
    charts = os.path.join(work_dir, "ppt", "charts")

    # 슬라이드1: 기본 정보
    update_slide1(os.path.join(slides, "slide1.xml"), data)

    # 슬라이드2: 텍스트 숫자
    update_slide2_text(os.path.join(slides, "slide2.xml"), data)

    # 도넛 차트 (경쟁상태불안 3개)
    update_donut_chart(os.path.join(charts, "chart4.xml"), data['cognitive_anxiety'])   # 인지불안
    update_donut_chart(os.path.join(charts, "chart5.xml"), data['state_confidence'])    # 상태자신감
    update_donut_chart(os.path.join(charts, "chart6.xml"), data['somatic_anxiety'])     # 신체불안

    # 스포츠자신감 막대그래프
    update_bar_chart(
        os.path.join(charts, "chart7.xml"),
        data['sc_ability'], data['sc_social'], data['sc_coach'], data['sc_physical']
    )

    # 수행전략 레이더 차트
    update_radar_chart(
        os.path.join(charts, "chart8.xml"),
        data['ps_self_talk'], data['ps_auto'], data['ps_imagery'], data['ps_relax'],
        data['ps_goal'], data['ps_emotion'], data['ps_negative'], data['ps_distract']
    )

    # 슬라이드3: 규칙 기반 총평 생성 후 삽입
    commentary = data.get('commentary') or generate_commentary(data)
    update_slide3(os.path.join(slides, "slide3.xml"), data, commentary)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("사용법: python generate_ppt.py [엑셀] [PPT템플릿] [선수명] [출력폴더]")
        sys.exit(1)
    generate_ppt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv)>4 else ".")



"""규칙 기반 총평 생성기 - 김선우 총평 스타일 기준"""


# ── 메인 생성 함수 ────────────────────────────────────────────────────────────

def generate_ppt_bytes(pptx_bytes, data):
    """pptx_bytes를 받아 수정된 pptx bytes 반환 (Streamlit용)"""
    import tempfile
    work_dir = tempfile.mkdtemp()
    try:
        with zipfile.ZipFile(BytesIO(pptx_bytes)) as z:
            z.extractall(work_dir)
        _apply_data(work_dir, data)
        buf = BytesIO()
        with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
            for root, dirs, files in os.walk(work_dir):
                for file in files:
                    fp = os.path.join(root, file)
                    z.write(fp, os.path.relpath(fp, work_dir))
        buf.seek(0)
        return buf.read()
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)

def generate_ppt(excel_path, template_path, athlete_name, output_dir="."):
    """파일 경로로 직접 실행 (CLI용)"""
    data = load_athlete_data(excel_path, athlete_name)
    print(f"✅ {data['name']} | {data['sport']} | {data['dob_year']}년 {data['dob_month']:02d}월 {data['dob_day']:02d}일")

    work_dir = f"/tmp/ppt_{athlete_name}"
    if os.path.exists(work_dir): shutil.rmtree(work_dir)
    os.system(f"python /mnt/skills/public/pptx/scripts/office/unpack.py '{template_path}' '{work_dir}' 2>/dev/null")
    _apply_data(work_dir, data)
    os.makedirs(output_dir, exist_ok=True)
    today = datetime.today().strftime("%Y%m%d")
    sport_safe = re.sub(r'[,/ ]','_', data['sport']).strip('_')
    out = os.path.join(output_dir, f"{today}_{sport_safe}_{athlete_name}_멘탈프로파일.pptx")
    os.system(f"python /mnt/skills/public/pptx/scripts/office/pack.py '{work_dir}' '{out}' --original '{template_path}' 2>/dev/null")
    shutil.rmtree(work_dir)
    print(f"✨ 완료 → {out}")
    return out, data

def _apply_data(work_dir, data):
    """실제 데이터 적용 (공통)"""
    slides = os.path.join(work_dir, "ppt", "slides")
    charts = os.path.join(work_dir, "ppt", "charts")

    # 슬라이드1: 기본 정보
    update_slide1(os.path.join(slides, "slide1.xml"), data)

    # 슬라이드2: 텍스트 숫자
    update_slide2_text(os.path.join(slides, "slide2.xml"), data)

    # 도넛 차트 (경쟁상태불안 3개)
    update_donut_chart(os.path.join(charts, "chart4.xml"), data['cognitive_anxiety'])   # 인지불안
    update_donut_chart(os.path.join(charts, "chart5.xml"), data['state_confidence'])    # 상태자신감
    update_donut_chart(os.path.join(charts, "chart6.xml"), data['somatic_anxiety'])     # 신체불안

    # 스포츠자신감 막대그래프
    update_bar_chart(
        os.path.join(charts, "chart7.xml"),
        data['sc_ability'], data['sc_social'], data['sc_coach'], data['sc_physical']
    )

    # 수행전략 레이더 차트
    update_radar_chart(
        os.path.join(charts, "chart8.xml"),
        data['ps_self_talk'], data['ps_auto'], data['ps_imagery'], data['ps_relax'],
        data['ps_goal'], data['ps_emotion'], data['ps_negative'], data['ps_distract']
    )

    # 슬라이드3: 규칙 기반 총평 생성 후 삽입
    commentary = data.get('commentary') or generate_commentary(data)
    update_slide3(os.path.join(slides, "slide3.xml"), data, commentary)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("사용법: python generate_ppt.py [엑셀] [PPT템플릿] [선수명] [출력폴더]")
        sys.exit(1)
    generate_ppt(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4] if len(sys.argv)>4 else ".")



"""규칙 기반 총평 생성기 - 김선우 총평 스타일 기준"""

# ── 수준 판단 함수 ─────────────────────────────────────────────────────────────

def level_30(val):
    """30점 만점 기준 수준"""
    if val >= 23: return "high"
    elif val >= 15: return "mid"
    else: return "low"

def level_sc(val):
    """스포츠자신감 5점 만점 (높을수록 좋음)"""
    if val >= 4.8: return "perfect"    # 만점/매우 이상적
    elif val >= 4.0: return "high"     # 높음
    elif val >= 3.0: return "mid"      # 보통
    else: return "low"                 # 낮음

def level_pos(val):
    """수행전략 긍정 (높을수록 좋음)"""
    if val >= 4.8: return "perfect"
    elif val >= 4.0: return "high"
    elif val >= 3.0: return "mid"
    else: return "low"

def level_neg(val):
    """수행전략 부정 (낮을수록 좋음)"""
    if val <= 1.5: return "perfect"    # 이상적
    elif val <= 2.5: return "good"     # 양호
    elif val <= 3.5: return "fair"     # 다소 높음
    else: return "high"                # 높음


# ── 단락 생성 함수 ────────────────────────────────────────────────────────────

def para1_overall_optimism(data):
    """①전반 총평 + 낙관성"""
    name = data['name']
    opt = data['optimism']
    opt_lv = level_30(opt)

    # 전반 인상 결정 (불안/자신감 종합)
    ta = data['trait_anxiety']
    ca = data['cognitive_anxiety']
    sa = data['somatic_anxiety']
    sc = data['state_confidence']
    avg_anxiety = (ca + sa) / 2
    
    if avg_anxiety <= 13 and sc >= 20 and ta <= 17:
        overall = "전반적으로 심리적으로 매우 안정되고 준비된 상태임을 보여주고 있습니다."
    elif avg_anxiety <= 17 and sc >= 17:
        overall = "전반적으로 심리적 준비 상태가 양호한 편으로 나타났습니다."
    elif avg_anxiety >= 20 or sc <= 14:
        overall = "전반적으로 시합 상황에서 심리적 부담과 긴장을 크게 느끼는 편으로 나타났습니다."
    else:
        overall = "전반적으로 일부 영역에서 심리적 지원이 필요한 것으로 나타났습니다."

    # 낙관성 표현
    opt_texts = {
        "high": "낙관성이 높게 나타나 어려운 상황에서도 긍정적으로 해석하고 회복하는 심리적 자원이 잘 갖춰져 있습니다.",
        "mid": "낙관성은 중간 수준으로 나타나 어려운 상황에서도 긍정적인 방향으로 해석하려는 기본적인 경향이 갖춰져 있습니다.",
        "low": "낙관성이 다소 낮게 나타나 어려운 상황에서 부정적으로 해석하거나 위축될 가능성이 있어 주의가 필요합니다.",
    }
    return f"{name} 선수의 스포츠심리측정 결과, {overall} {opt_texts[opt_lv]}"


def para2_anxiety(data):
    """②특성불안 + 상태불안"""
    ta_lv = level_30(data['trait_anxiety'])
    ca_lv = level_30(data['cognitive_anxiety'])
    sa_lv = level_30(data['somatic_anxiety'])
    sc_lv = level_30(data['state_confidence'])

    # 특성불안
    ta_texts = {
        "high": "스포츠경쟁불안(특성불안)이 높게 나타나, 중요한 경기일수록 압박감이 크게 작용하거나 경기 전부터 부담을 많이 느낄 수 있습니다.",
        "mid": "스포츠경쟁불안(특성불안)은 중간 수준으로, 중요한 경기에서 일정한 긴장이나 부담을 느낄 수 있으나 수행을 방해할 정도로 크지는 않은 편입니다.",
        "low": "스포츠경쟁불안(특성불안)이 낮게 나타나, 경쟁 상황에서도 비교적 안정적으로 심리 상태를 유지하는 편입니다.",
    }

    # 인지/신체불안 조합
    if ca_lv == "low" and sa_lv == "low":
        anx_text = "상태불안 결과에서는 인지적 불안과 신체적 불안 모두 낮게 나타났습니다."
    elif ca_lv == "high" and sa_lv == "high":
        anx_text = "상태불안 결과에서는 인지적 불안과 신체적 불안 모두 높게 나타나, 경기 전후로 생각이 많아지고 몸의 긴장도 함께 올라오는 형태가 나타날 수 있습니다."
    elif ca_lv == "high":
        anx_text = "상태불안 결과에서는 인지적 불안이 높게 나타나 경기 전후로 생각이 많아지거나 걱정이 커지는 형태가 나타날 수 있으며, 신체적 불안은 비교적 양호한 수준입니다."
    elif sa_lv == "high":
        anx_text = "상태불안 결과에서는 신체적 불안이 높게 나타나 몸의 긴장이 심하게 올라올 수 있으며, 인지적 불안은 비교적 양호한 수준입니다."
    else:
        anx_text = "상태불안 결과에서는 인지적 불안과 신체적 불안 모두 중간 수준으로 나타났습니다."

    # 상태자신감
    sc_texts = {
        "high": "상태 자신감이 높게 나타나 경기 상황에서 자기 확신이 강점으로 작용할 수 있습니다.",
        "mid": "상태 자신감은 중간 수준으로 나타났습니다.",
        "low": "상태 자신감이 낮게 나타나, 긴장 상황에서 '할 수 있다'는 마음을 유지하는 것이 쉽지 않을 수 있습니다.",
    }

    return f"{ta_texts[ta_lv]} {anx_text} {sc_texts[sc_lv]}"


def para3_sport_confidence(data):
    """③스포츠 자신감"""
    scores = {
        '능력입증': data['sc_ability'],
        '코치 지도력': data['sc_coach'],
        '사회적 지지': data['sc_social'],
        '신체·정신적 준비': data['sc_physical'],
    }
    levels = {k: level_sc(v) for k, v in scores.items()}

    perfect = [k for k, lv in levels.items() if lv == "perfect"]
    high = [k for k, lv in levels.items() if lv == "high"]
    mid = [k for k, lv in levels.items() if lv == "mid"]
    low = [k for k, lv in levels.items() if lv == "low"]

    # 모두 만점
    if len(perfect) == 4:
        return ("스포츠 자신감(자신감의 원천)에서는 능력입증, 코치 지도력, 사회적 지지, 신체·정신적 준비 요인이 모두 만점으로 나타났습니다. "
                "이는 훈련 과정에서의 준비감과 코치에 대한 신뢰, 주변의 응원 등 자신감을 구성하는 모든 요소가 매우 탄탄하게 갖춰져 있음을 의미합니다.")

    # 모두 높음 이상
    if len(perfect) + len(high) == 4:
        names = list(scores.keys())
        return (f"스포츠 자신감(자신감의 원천)에서는 {', '.join(names)} 요인 모두 높게 나타났습니다. "
                "자신감을 구성하는 전반적인 요소들이 잘 갖춰져 있어 경기 상황에서 안정적인 자신감을 발휘할 수 있을 것입니다.")

    # 강점/약점 혼합
    good = perfect + high
    weak = low + mid

    if good and weak:
        good_str = ', '.join(good)
        weak_str = ', '.join(weak)
        return (f"스포츠 자신감(자신감의 원천)에서는 {good_str} 요인이 높게 나타난 반면, "
                f"{weak_str}이(가) 다소 낮게 나타났습니다. "
                f"{weak_str} 측면에서의 자신감이 충분히 형성될 수 있도록 지속적인 관심이 필요합니다.")
    elif not weak:
        return ("스포츠 자신감(자신감의 원천)에서는 전반적으로 양호한 수준으로 나타났습니다. "
                "자신감의 다양한 원천이 고루 갖춰져 있어 경기 상황에서 안정적인 자신감을 유지할 수 있을 것입니다.")
    else:
        weak_str = ', '.join(weak)
        return (f"스포츠 자신감(자신감의 원천)에서는 전반적으로 발달이 필요한 것으로 나타났습니다. "
                f"특히 {weak_str} 측면의 자신감을 높이기 위한 체계적인 지원이 필요합니다.")


def para4_performance_strategy(data):
    """④수행전략 + 실천 제언"""
    pos = {
        '혼잣말': data['ps_self_talk'],
        '자동적수행': data['ps_auto'],
        '심상': data['ps_imagery'],
        '긴장풀기': data['ps_relax'],
        '목표설정': data['ps_goal'],
    }
    neg = {
        '부정적 생각': data['ps_negative'],
        '주의산만': data['ps_distract'],
        '감정조절': data['ps_emotion'],
    }

    pos_levels = {k: level_pos(v) for k, v in pos.items()}
    neg_levels = {k: level_neg(v) for k, v in neg.items()}

    # 긍정 전략 분류
    pos_ideal = [k for k, lv in pos_levels.items() if lv in ("perfect", "high")]
    pos_weak = [k for k, lv in pos_levels.items() if lv in ("mid", "low")]

    # 부정 전략 분류
    neg_ideal = [k for k, lv in neg_levels.items() if lv in ("perfect", "good")]
    neg_concern = [k for k, lv in neg_levels.items() if lv in ("fair", "high")]

    parts = []

    # 긍정 전략 표현
    if len(pos_ideal) >= 4:
        parts.append(f"수행전략에서는 {', '.join(pos_ideal)} 전략이 이상적인 수준에 가깝게 잘 활용되고 있습니다.")
    elif pos_ideal:
        parts.append(f"수행전략에서는 {', '.join(pos_ideal)}이(가) 비교적 잘 활용되고 있습니다.")
    else:
        parts.append("수행전략 전반에서 추가적인 발달이 필요한 것으로 나타났습니다.")

    if pos_weak:
        parts.append(f"{', '.join(pos_weak)}은(는) 이상적인 수준에 비해 다소 부족하게 나타났습니다.")

    # 부정 전략 + 실천 제언
    if neg_concern:
        concern_str = ', '.join(neg_concern)
        if '부정적 생각' in neg_concern and '주의산만' in neg_concern:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 다소 높게 나타나, "
                      "경기 흐름이 꼬이거나 실수가 발생하는 상황에서 집중력이 흔들리거나 부정적인 생각이 유입될 수 있습니다. "
                      "실수 후 빠르게 현재에 집중하는 루틴을 훈련 과정에서 꾸준히 연습한다면 경기 운영에 도움이 될 것입니다.")
        elif '부정적 생각' in neg_concern:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 높게 나타나, "
                      "경기 중 부정적인 생각이 수행에 영향을 줄 수 있습니다. "
                      "부정적인 생각을 인식하고 전환하는 심리기술 훈련을 체계적으로 익혀나가길 권장합니다.")
        elif '주의산만' in neg_concern:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 높게 나타나, "
                      "경기 상황에서 집중력이 흔들릴 수 있습니다. "
                      "루틴 개발과 주의 집중 훈련을 통해 집중력을 강화하는 것을 권장합니다.")
        else:
            advice = (f"다만 {concern_str}이(가) 이상적인 수준보다 높게 나타났습니다. "
                      "스포츠심리상담을 통해 개인에게 맞는 심리기술을 체계적으로 익혀나가길 권장합니다.")
        parts.append(advice)
    else:
        parts.append("부정적 생각과 주의산만도 이상적인 수준으로 잘 관리되고 있어, "
                     "지속적인 심리기술 훈련을 통해 현재의 강점을 더욱 공고히 하는 것을 권장합니다.")

    return " ".join(parts)


def generate_commentary(data):
    """4단락 총평 생성 (줄바꿈으로 구분)"""
    p1 = para1_overall_optimism(data)
    p2 = para2_anxiety(data)
    p3 = para3_sport_confidence(data)
    p4 = para4_performance_strategy(data)
    return f"{p1}\n{p2}\n{p3}\n{p4}"