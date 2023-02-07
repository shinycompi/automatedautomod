from datetime import datetime

def automod_text_from_file(file_name):
    with open(file_name) as file:
        return file.read()
    
def rule_list_from_line(line):
    rule_list = line.split()
    rule_list.remove("rule-start")
    rule_list.remove("#")
    return rule_list

def utc_weekday_num():
    return datetime.utcnow().weekday()

def utc_weekday_str():    
    return datetime.utcnow().strftime('%A')

def day_rule_text_from_weekday_num(day_num):
    day_rule_names = ["mon-off", "tue-off", "wed-off", "thu-off", "fri-off", "sat-off", "sun-off"]
    return day_rule_names[day_num]

def disable_rule(rule, automod_lines):
    i = rule["start_line"] - 1
    while i < rule["end_line"]:
        if not automod_lines[i].strip().startswith("#"):
            automod_lines[i] = "#" + automod_lines[i]
        i = i + 1
    return automod_lines

def enable_rule(rule, automod_lines):
    i = rule["start_line"] - 1
    while i < rule["end_line"]:
        if automod_lines[i].strip().startswith("#"):
            automod_lines[i] = automod_lines[i].strip("#")
        i = i + 1
    return automod_lines

def create_rule_blocks(lines):
    rule_blocks = []
    i = 0
    start_line = 0
    end_line = 0
    rule_list = []
    for line in lines:
        if "rule-start" in line:
            start_line = i
            rule_list = rule_list_from_line(line)
        if "rule-end" in line:
            end_line = i
            rule_blocks.append({"rule_list": rule_list, "start_line": start_line + 2, "end_line": end_line})
        i = i + 1
    return rule_blocks

def apply_rules_to_automod_lines(rule_blocks, automod_lines):
    for rule in rule_blocks:
        if day_rule_text_from_weekday_num(utc_weekday_num()) in rule["rule_list"]:
            automod_lines = disable_rule(rule, automod_lines)
        else:
            automod_lines = enable_rule(rule, automod_lines)
    return automod_lines

def write_automod_to_file(automod, file_name):
    with open(file_name, "w") as file:
        file.write(automod)
