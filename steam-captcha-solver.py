import capsolver
from urllib.parse import urlparse

# Change this information
PARSED_PROXY = "http://username:password@host:port"

capsolver.api_key = "Your pay per usage key"

def solve_recaptcha_v2_enterprise():
    solution = capsolver.solve({
      "type": "ReCaptchaV2EnterpriseTask",
        "websiteURL": "https://store.steampowered.com",
        "websiteKey": "6LdIFr0ZAAAAAO3vz0O0OQrtAefzdJcWQM2TMYQH",
        "enterprisePayload": {
            "s": "This value changes everytime"
        },
        "proxy": PARSED_PROXY
    })
    return solution

def main():
    
    print("Solving steam captcha")
    solution = solve_recaptcha_v2_enterprise()
    
    token = solution["gRecaptchaResponse"]
    
    print("Token Solution " + token)
    
if __name__ == "__main__":
    main()
