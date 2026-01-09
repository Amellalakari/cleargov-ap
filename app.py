import streamlit as st

st.set_page_config(page_title="ClearGov AP", layout="centered")

# Language toggle
language = st.radio("Language / భాష", ["English", "తెలుగు"], horizontal=True)
lang = "en" if language == "English" else "te"

# App content
content = {
    "title": {"en": "ClearGov AP", "te": "క్లియర్ గవ్ ఏపీ"},
    "subtitle": {
        "en": "Clear guidance for Andhra Pradesh government certificates",
        "te": "ఆంధ్రప్రదేశ్ ప్రభుత్వ ధృవీకరణ పత్రాల కోసం స్పష్టమైన మార్గదర్శకం"
    },
    "income": {
        "name": {"en": "Income Certificate", "te": "ఆదాయ ధృవీకరణ పత్రం"},
        "what": {
            "en": "An Income Certificate is an official document issued by the Government of Andhra Pradesh showing a family’s annual income.",
            "te": "ఆదాయ ధృవీకరణ పత్రం అనేది ఆంధ్రప్రదేశ్ ప్రభుత్వం జారీ చేసే అధికారిక పత్రం. ఇది కుటుంబం యొక్క వార్షిక ఆదాయాన్ని చూపిస్తుంది."
        },
        "steps": {
            "en": [
                "Visit MeeSeva or apply online",
                "Fill application form",
                "Submit documents",
                "Pay fee",
                "Verification by Village Secretariat",
                "Approval by Tahsildar",
                "Download certificate"
            ],
            "te": [
                "మీ సేవ కేంద్రానికి వెళ్లండి లేదా ఆన్‌లైన్‌లో దరఖాస్తు చేయండి",
                "దరఖాస్తు ఫారం పూరించండి",
                "పత్రాలు సమర్పించండి",
                "ఫీజు చెల్లించండి",
                "గ్రామ సచివాలయం ద్వారా ధృవీకరణ",
                "తహసీల్దార్ ఆమోదం",
                "సర్టిఫికెట్ డౌన్‌లోడ్ చేయండి"
            ]
        }
    },
    "disclaimer": {
        "en": "This app provides guidance only. Always verify with official sources.",
        "te": "ఈ యాప్ కేవలం మార్గదర్శక సమాచారం మాత్రమే అందిస్తుంది. అధికారిక వనరులతో నిర్ధారించుకోండి."
    }
}

# UI rendering
st.title(content["title"][lang])
st.caption(content["subtitle"][lang])
st.divider()

st.header(content["income"]["name"][lang])
st.write(content["income"]["what"][lang])

st.subheader("Step-by-step process" if lang == "en" else "దశల వారీ ప్రక్రియ")
for i, step in enumerate(content["income"]["steps"][lang], start=1):
    st.write(f"{i}. {step}")

st.divider()
st.caption(content["disclaimer"][lang])



