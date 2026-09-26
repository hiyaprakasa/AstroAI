import streamlit as st
from datetime import date


# ============================================================
# PAGE SETTINGS
# ============================================================

st.set_page_config(
    page_title="AstroAI",
    page_icon="✨",
    layout="centered"
)


# ============================================================
# ZODIAC DATA
# ============================================================

zodiac_data = {
    "Aries": {
        "emoji": "♈",
        "personality": (
            "You tend to have an energetic, independent and action-oriented "
            "personality. You may naturally take initiative and prefer to "
            "move forward rather than wait for others."
        ),
        "career": (
            "You may enjoy careers that provide independence, leadership, "
            "competition and opportunities to take initiative. Roles involving "
            "management, entrepreneurship, technology, sales or project "
            "leadership may feel engaging."
        ),
        "love": (
            "In relationships, you may value honesty, excitement and direct "
            "communication. You may prefer relationships where both people "
            "have independence while still supporting each other."
        ),
        "finance": (
            "You may be comfortable taking action with money, but planning "
            "and patience can help you make more consistent financial decisions. "
            "Avoid making financial decisions purely from impulse."
        ),
        "family": (
            "You may have a protective and straightforward approach toward "
            "people you care about. You may sometimes need to balance your "
            "independence with the needs of family members."
        ),
        "travel": (
            "You may enjoy travel that involves exploration, activity and new "
            "experiences. Independent trips or discovering unfamiliar places "
            "may be particularly interesting."
        ),
        "strengths": "Confidence, initiative, courage, independence and enthusiasm.",
        "challenges": "Impatience, impulsiveness and becoming frustrated when progress is slow."
    },

    "Taurus": {
        "emoji": "♉",
        "personality": (
            "You may have a practical, patient and steady personality. You "
            "often appreciate stability, comfort and situations where you "
            "can build something gradually."
        ),
        "career": (
            "You may perform well in environments that reward consistency, "
            "practical thinking and long-term effort. Finance, business, "
            "design, technology, administration and management can be areas "
            "where these qualities are useful."
        ),
        "love": (
            "You may value loyalty, trust and emotional stability in relationships. "
            "Once you become comfortable with someone, you may prefer building "
            "a relationship slowly and securely."
        ),
        "finance": (
            "You may naturally appreciate financial security and long-term "
            "planning. Consistent saving and avoiding unnecessary impulsive "
            "spending can support your financial goals."
        ),
        "family": (
            "Family stability may be important to you. You may show affection "
            "through practical support, reliability and being present when "
            "others need you."
        ),
        "travel": (
            "You may enjoy comfortable travel where accommodation, food and "
            "planning are well organized. Scenic destinations and relaxing "
            "experiences may appeal to you."
        ),
        "strengths": "Patience, loyalty, reliability, determination and practicality.",
        "challenges": "Stubbornness, resistance to change and becoming too attached to comfort."
    },

    "Gemini": {
        "emoji": "♊",
        "personality": (
            "You may be curious, adaptable and interested in learning new "
            "things. Communication and exchanging ideas may play an important "
            "role in your personality."
        ),
        "career": (
            "You may enjoy careers involving communication, technology, "
            "writing, marketing, analysis, networking or learning. Jobs that "
            "offer variety may keep you more engaged than repetitive work."
        ),
        "love": (
            "Mental connection and communication may be especially important "
            "to you in relationships. You may appreciate a partner who can "
            "communicate openly and share different interests."
        ),
        "finance": (
            "You may have many ideas for earning or using money. Creating a "
            "clear financial plan can help prevent scattered decision-making."
        ),
        "family": (
            "You may enjoy conversations and sharing ideas with family. "
            "Keeping communication open can help you maintain strong connections."
        ),
        "travel": (
            "You may enjoy exploring multiple places and meeting different "
            "people. Short trips and destinations with cultural or educational "
            "experiences may be appealing."
        ),
        "strengths": "Communication, curiosity, adaptability, intelligence and networking.",
        "challenges": "Overthinking, inconsistency and losing interest too quickly."
    },

    "Cancer": {
        "emoji": "♋",
        "personality": (
            "You may be emotionally intuitive, caring and strongly connected "
            "to people and places that feel familiar. Your emotional environment "
            "may influence your decisions significantly."
        ),
        "career": (
            "You may appreciate careers where empathy, responsibility and "
            "supporting others are valuable. Education, healthcare, management, "
            "hospitality, psychology and people-focused roles may appeal to you."
        ),
        "love": (
            "Emotional security and trust may be important in relationships. "
            "You may prefer a connection that feels safe, supportive and genuine."
        ),
        "finance": (
            "You may value financial security because it creates a sense of "
            "stability. Long-term planning may be more comfortable than "
            "highly unpredictable financial decisions."
        ),
        "family": (
            "Family and emotional bonds may be especially meaningful to you. "
            "You may naturally take a caring or protective role within the family."
        ),
        "travel": (
            "You may enjoy destinations that provide emotional comfort, nature "
            "or meaningful experiences rather than simply traveling for excitement."
        ),
        "strengths": "Empathy, loyalty, intuition, caring nature and emotional awareness.",
        "challenges": "Sensitivity, holding onto the past and mood-based decision-making."
    },

    "Leo": {
        "emoji": "♌",
        "personality": (
            "You may have a confident, expressive and warm personality. "
            "Recognition, creativity and the ability to express yourself may "
            "be important to you."
        ),
        "career": (
            "You may enjoy positions where you can lead, present ideas, "
            "create something or take responsibility. Management, media, "
            "business, entertainment, design and leadership-oriented careers "
            "may suit these qualities."
        ),
        "love": (
            "You may value affection, loyalty and appreciation in relationships. "
            "You may enjoy expressing love openly and may appreciate a partner "
            "who recognizes your efforts."
        ),
        "finance": (
            "You may enjoy spending on experiences, appearance or things you "
            "value. Maintaining a balance between enjoyment and long-term "
            "financial planning can be useful."
        ),
        "family": (
            "You may naturally take a visible or supportive role within the "
            "family. Appreciation and mutual respect can be particularly "
            "important in family relationships."
        ),
        "travel": (
            "You may enjoy memorable destinations, celebrations and experiences "
            "that allow you to explore and express yourself."
        ),
        "strengths": "Confidence, creativity, leadership, generosity and enthusiasm.",
        "challenges": "Pride, sensitivity to criticism and wanting recognition."
    },

    "Virgo": {
        "emoji": "♍",
        "personality": (
            "You may be analytical, organized and detail-oriented. You may "
            "prefer understanding how something works before making important "
            "decisions."
        ),
        "career": (
            "You may enjoy work involving analysis, organization, technology, "
            "research, quality control, healthcare, finance or problem-solving."
        ),
        "love": (
            "You may express affection through practical support and reliability. "
            "Trust may develop gradually, and you may appreciate consistency "
            "more than dramatic gestures."
        ),
        "finance": (
            "You may naturally pay attention to details and practical financial "
            "planning. Budgeting and structured saving can work well with this approach."
        ),
        "family": (
            "You may show care by helping family members solve problems and "
            "taking responsibility when necessary."
        ),
        "travel": (
            "You may enjoy well-planned trips where schedules and important "
            "details are organized in advance."
        ),
        "strengths": "Analysis, organization, reliability, discipline and attention to detail.",
        "challenges": "Overthinking, perfectionism and being overly critical of yourself."
    },

    "Libra": {
        "emoji": "♎",
        "personality": (
            "You may value balance, harmony and good communication. You may "
            "naturally consider different perspectives before making decisions."
        ),
        "career": (
            "You may enjoy careers involving communication, negotiation, "
            "design, consulting, public relations, business or collaboration."
        ),
        "love": (
            "Partnership and emotional balance may be important to you. You may "
            "prefer relationships where both people communicate respectfully "
            "and contribute equally."
        ),
        "finance": (
            "You may enjoy spending on aesthetics, experiences and social activities. "
            "Maintaining a structured budget can help balance enjoyment and saving."
        ),
        "family": (
            "You may often try to maintain peace within your family. Open "
            "communication can help you avoid carrying other people's conflicts."
        ),
        "travel": (
            "You may enjoy beautiful destinations, cultural experiences and "
            "travel with people whose company you value."
        ),
        "strengths": "Diplomacy, communication, fairness, creativity and cooperation.",
        "challenges": "Indecision, people-pleasing and avoiding difficult conversations."
    },

    "Scorpio": {
        "emoji": "♏",
        "personality": (
            "You may have an intense, focused and private personality. When "
            "something matters to you, you may invest significant energy into it."
        ),
        "career": (
            "You may enjoy careers involving research, investigation, technology, "
            "psychology, finance, strategy or complex problem-solving."
        ),
        "love": (
            "Trust and emotional depth may be very important to you. You may "
            "prefer meaningful connections rather than superficial relationships."
        ),
        "finance": (
            "You may approach important financial decisions carefully when you "
            "have enough information. Long-term strategy may appeal to you."
        ),
        "family": (
            "You may be deeply protective of people you consider close. "
            "Trust and loyalty can play an important role in family connections."
        ),
        "travel": (
            "You may enjoy destinations with history, mystery, nature or "
            "opportunities for deep exploration."
        ),
        "strengths": "Focus, determination, loyalty, resilience and strategic thinking.",
        "challenges": "Being overly private, holding grudges and becoming too intense."
    },

    "Sagittarius": {
        "emoji": "♐",
        "personality": (
            "You may be optimistic, adventurous and interested in discovering "
            "new ideas and experiences. Freedom and personal growth may be important."
        ),
        "career": (
            "You may enjoy careers involving travel, education, technology, "
            "consulting, communication, business or international environments."
        ),
        "love": (
            "You may value honesty, freedom and friendship within relationships. "
            "A relationship that allows both people to grow may be especially meaningful."
        ),
        "finance": (
            "You may be optimistic about opportunities, but maintaining a "
            "structured savings plan can help balance enthusiasm with financial security."
        ),
        "family": (
            "You may bring enthusiasm and positivity to family relationships. "
            "At the same time, you may need personal space and independence."
        ),
        "travel": (
            "Travel may be a particularly meaningful source of learning and "
            "personal growth. International or long-distance travel may interest you."
        ),
        "strengths": "Optimism, independence, learning, adaptability and enthusiasm.",
        "challenges": "Restlessness, impatience and taking on too many things at once."
    },

    "Capricorn": {
        "emoji": "♑",
        "personality": (
            "You may be disciplined, responsible and focused on long-term goals. "
            "You may prefer building success gradually through consistent effort."
        ),
        "career": (
            "You may appreciate structured professional environments and roles "
            "that provide responsibility and opportunities for advancement."
        ),
        "love": (
            "You may take relationships seriously and value commitment and "
            "reliability. You may show affection through actions rather than words."
        ),
        "finance": (
            "Long-term financial planning may naturally appeal to you. "
            "You may prefer building stability rather than relying on short-term gains."
        ),
        "family": (
            "You may feel responsible for supporting family members. "
            "Learning to balance responsibility with personal needs can be important."
        ),
        "travel": (
            "You may prefer purposeful travel, such as trips connected to "
            "career, learning, family or long-term plans."
        ),
        "strengths": "Discipline, responsibility, patience, ambition and persistence.",
        "challenges": "Being too serious, work-related stress and putting excessive pressure on yourself."
    },

    "Aquarius": {
        "emoji": "♒",
        "personality": (
            "You may be independent, innovative and interested in unusual ideas. "
            "You may prefer thinking differently rather than simply following tradition."
        ),
        "career": (
            "Technology, research, innovation, social projects, data, engineering "
            "and creative problem-solving may appeal to your independent thinking."
        ),
        "love": (
            "Friendship and mental connection may be important in relationships. "
            "You may appreciate a partner who respects your independence."
        ),
        "finance": (
            "You may be interested in new ways of earning or managing money. "
            "A practical financial structure can help turn innovative ideas into stability."
        ),
        "family": (
            "You may care deeply about family while still needing personal space. "
            "Respecting different viewpoints can strengthen family relationships."
        ),
        "travel": (
            "You may enjoy unusual destinations, new cultures, technology-focused "
            "places and experiences that introduce fresh perspectives."
        ),
        "strengths": "Innovation, independence, originality, curiosity and problem-solving.",
        "challenges": "Detachment, unpredictability and difficulty with routine."
    },

    "Pisces": {
        "emoji": "♓",
        "personality": (
            "You may be imaginative, empathetic and emotionally perceptive. "
            "Creativity and intuition may play an important role in your life."
        ),
        "career": (
            "You may enjoy creative, helping or people-focused careers. "
            "Design, media, education, counseling, healthcare and creative technology "
            "can provide opportunities to use imagination and empathy."
        ),
        "love": (
            "Emotional connection and understanding may be very important to you. "
            "You may value compassion and a strong sense of emotional closeness."
        ),
        "finance": (
            "You may sometimes make financial decisions based on emotions or "
            "generosity. Clear financial boundaries and planning can be helpful."
        ),
        "family": (
            "You may be emotionally connected to family and naturally notice "
            "how others are feeling."
        ),
        "travel": (
            "You may enjoy peaceful, artistic, spiritual or nature-oriented "
            "destinations that give you time to reflect and recharge."
        ),
        "strengths": "Empathy, creativity, imagination, intuition and compassion.",
        "challenges": "Over-sensitivity, idealizing situations and difficulty setting boundaries."
    }
}


# ============================================================
# FUNCTION TO CALCULATE SUN SIGN
# ============================================================

def get_zodiac_sign(day, month):

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"

    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"

    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"

    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"

    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"

    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"

    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"

    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"

    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"

    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"

    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"

    else:
        return "Pisces"


# ============================================================
# MAIN PAGE
# ============================================================

st.title("✨ AstroAI")
st.subheader("Your AI Horoscope Guide")

st.write(
    "Enter your birth details to generate a detailed "
    "personalized horoscope report."
)

st.divider()


# ============================================================
# USER DETAILS
# ============================================================

st.header("🌙 Enter Your Birth Details")


# NAME

name = st.text_input(
    "Your Name",
    placeholder="Enter your name"
)


# ============================================================
# DATE OF BIRTH
# ============================================================

st.write("### 📅 Date of Birth")

date_col1, date_col2, date_col3 = st.columns(3)

with date_col1:
    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=1,
        step=1
    )

with date_col2:
    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=1,
        step=1
    )

with date_col3:
    year = st.number_input(
        "Year",
        min_value=1900,
        max_value=date.today().year,
        value=2000,
        step=1
    )


# ============================================================
# TIME OF BIRTH
# ============================================================

st.write("### 🕐 Time of Birth")

time_col1, time_col2, time_col3 = st.columns(3)

with time_col1:
    birth_hour = st.number_input(
        "Hour",
        min_value=1,
        max_value=12,
        value=1,
        step=1
    )

with time_col2:
    birth_minute = st.number_input(
        "Minute",
        min_value=0,
        max_value=59,
        value=25,
        step=1
    )

with time_col3:
    am_pm = st.selectbox(
        "AM / PM",
        ["AM", "PM"]
    )


# ============================================================
# PLACE OF BIRTH
# ============================================================

st.write("### 📍 Place of Birth")

place_of_birth = st.text_input(
    "Birth Place",
    placeholder="Example: Vijayawada, Andhra Pradesh, India"
)


st.divider()


# ============================================================
# GENERATE HOROSCOPE
# ============================================================

if st.button(
    "🔮 Generate Horoscope",
    use_container_width=True
):

    if not name:

        st.warning("Please enter your name.")

    elif not place_of_birth:

        st.warning("Please enter your place of birth.")

    else:

        try:

            # Validate date

            birth_date = date(
                int(year),
                int(month),
                int(day)
            )


            # Format time

            formatted_time = (
                f"{int(birth_hour):02d}:"
                f"{int(birth_minute):02d} "
                f"{am_pm}"
            )


            # Calculate zodiac sign

            zodiac_sign = get_zodiac_sign(
                int(day),
                int(month)
            )


            # Get zodiac information

            zodiac = zodiac_data[zodiac_sign]


            # ==================================================
            # SUCCESS
            # ==================================================

            st.success(
                "Your birth details have been successfully processed!"
            )


            # ==================================================
            # BIRTH INFORMATION
            # ==================================================

            st.header(
                f"✨ Horoscope for {name}"
            )

            st.write(
                f"**📅 Date of Birth:** "
                f"{birth_date.strftime('%d/%m/%Y')}"
            )

            st.write(
                f"**🕐 Time of Birth:** "
                f"{formatted_time}"
            )

            st.write(
                f"**📍 Place of Birth:** "
                f"{place_of_birth}"
            )


            st.divider()


            # ==================================================
            # SUN SIGN
            # ==================================================

            st.header(
                f"{zodiac['emoji']} Your Sun Sign: {zodiac_sign}"
            )

            st.write(
                f"Based on your date of birth, your Sun Sign is "
                f"**{zodiac_sign}**."
            )


            st.divider()


            # ==================================================
            # PERSONALITY
            # ==================================================

            st.subheader("🌞 Personality")

            st.write(
                zodiac["personality"]
            )


            # ==================================================
            # CAREER
            # ==================================================

            st.subheader("💼 Career & Professional Life")

            st.write(
                zodiac["career"]
            )


            # ==================================================
            # LOVE
            # ==================================================

            st.subheader("❤️ Love & Relationships")

            st.write(
                zodiac["love"]
            )


            # ==================================================
            # FINANCE
            # ==================================================

            st.subheader("💰 Finance")

            st.write(
                zodiac["finance"]
            )


            # ==================================================
            # FAMILY
            # ==================================================

            st.subheader("🏠 Family & Home")

            st.write(
                zodiac["family"]
            )


            # ==================================================
            # TRAVEL
            # ==================================================

            st.subheader("✈️ Travel & Foreign Opportunities")

            st.write(
                zodiac["travel"]
            )


            # ==================================================
            # STRENGTHS
            # ==================================================

            st.subheader("🌟 Your Strengths")

            st.write(
                zodiac["strengths"]
            )


            # ==================================================
            # CHALLENGES
            # ==================================================

            st.subheader("🌱 Areas for Growth")

            st.write(
                zodiac["challenges"]
            )


            # ==================================================
            # GENERAL GUIDANCE
            # ==================================================

            st.subheader("🔮 General Guidance")

            st.write(
                f"Your {zodiac_sign} Sun Sign suggests themes around "
                f"self-expression, personal development and relationships. "
                f"Use these interpretations as a tool for reflection rather "
                f"than as fixed predictions about your future."
            )


            # ==================================================
            # IMPORTANT NOTE
            # ==================================================

            st.divider()

            st.info(
                "✨ This is currently a basic Sun-Sign horoscope. "
                "The next version of AstroAI can calculate your complete "
                "birth chart, including the Moon Sign, Ascendant, houses "
                "and planetary positions, and then use AI to generate "
                "a much more detailed interpretation."
            )


        except ValueError:

            st.error(
                "The date you entered is not valid. "
                "For example, February cannot have 30 days. "
                "Please check your Day, Month and Year."
            )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "✨ AstroAI provides astrological interpretations "
    "for personal reflection and entertainment."
)