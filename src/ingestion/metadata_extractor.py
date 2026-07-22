import re


def detect_document(text):

    if "Arquitectura de Microservicios" in text:
        return "arquitectura"

    if "Ingeniería Back-end" in text:
        return "backend"

    if "Ingeniería Front-end" in text:
        return "frontend"

    if "Onboarding" in text:
        return "onboarding"

    if "Incidentes" in text:
        return "incidentes"

    return "general"


def detect_section(text):

    patterns = [
        r"^\d+\.\d+\.\d+\s+(.+)",
        r"^\d+\.\d+\s+(.+)",
        r"^SECCIÓN\s+\d+\s*[—-]\s*(.+)"
    ]

    lines = text.split("\n")

    for line in lines[:20]:

        line = line.strip()

        for pattern in patterns:

            match = re.match(
                pattern,
                line,
                re.IGNORECASE
            )

            if match:
                return line

    return "general"