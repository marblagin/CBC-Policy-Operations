import os
import sys


def policy_ops(id, key):
    token = str(key) + "/" + str(id)

    name_list = [
        "01 Good Protection",
        "02 Better Protection",
        "03 Best Protection",
        "04 Win-POC-Restrictive-Policy",
        "05 MacOS Basic Protection",
        "06 MacOS Advanced Protection"
    ]

    desc_list = [
        "Recommended for initial deployment to protect against Known Malware, Suspected Malware/PUP/Adware/, "
        "Zero-day Ransomware and Document-based Attacks using a combination of 5 Prevention techniques in a single "
        "agent. Ideal for Protection against Known Threats, as well as Baselining at the same time to detect "
        "legitimate/in-house developed applications behaving like rogue processes for false positives reduction.",
        "Added rules on top of Basic Protection Policy to protect against Living Off the Land Binaries attacks. These "
        "binaries may include legitimate tools like powershell, certutil, regsvr32, wmi been exploited. False "
        "positives may be observed which will require whitelisting.",
        "Recommended for Malware Testing Scenarios. You can copy some of the rules associated with mshta,msbuild, "
        "rundll32 to protect against advanced attacks involving pen testing tools into your production policies.",
        "Test policy for POCs, designed to be quite restrictive on test machines.",
        "Basic level of protection for MacOS Machines that also covers malicious behaviours coming from "
        "macro-embedded documents.",
        "An advanced set of blocking and isolation rules building on top of the MacOS Basic policy. This includes "
        "preventing malicious behaviours being performed from common directories such as downloads, desktop and temp."
    ]

    json_list = [
        "SamplePolicy_POC_01_Good_Protection.json",
        "SamplePolicy_POC_02_Better_Protection.json",
        "SamplePolicy_POC_03_Best_Protection.json",
        "SamplePolicy_POC_04_Win-POC-Restrictive-Policy.json",
        "SamplePolicy_POC_05_MacOS-POC-Basic.json",
        "SamplePolicy_POC_06_MacOS-POC-Advanced.json"
    ]

    for x in range(6):
        policy_command = "python policy_operations.py --cburl https://api-prod06.conferdeploy.net --apitoken " + \
                  token + " import -N \"" + name_list[x] + "\" -d \"" + desc_list[x] + "\" -p \"MEDIUM\" -f " + \
                         json_list[x] + "\""
        print("Adding policy " + str(name_list[x]))
        os.system(policy_command)


def main():
    policy_ops(input("Enter in API ID: "), input("Enter in API Key: "))


if __name__ == '__main__':
    sys.exit(main())
