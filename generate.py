def write(state, read, replace, direction, newState):
    with open("pi.tur", "a", encoding="utf-8") as pi:
        arrow = "\u2190" if direction == "<" else "→"
        pi.write("\u0394(%s,%s) = (%s,%s,%s)\n" % (state, read, replace, arrow, newState))

with open("pi.tur", "w") as pi:
    pi.write("")

digits = [str(i) for i in range(10)]

#Set up the calculation environment
for digit in digits:
    write("start", digit, digit, ">", "start")
write("start", "", "]", "<", "decrement_digit_counter")

for i, digit in enumerate(digits[1:]):
    write("decrement_digit_counter", digit, digits[i], ">", "nudge_end_marker")

write("decrement_digit_counter", "0", "9", "<", "decrement_digit_counter")
write("decrement_digit_counter", "", "", ">", "digit_counter_zero")
write("digit_counter_zero", "9", "", ">", "digit_counter_zero")
write("digit_counter_zero", "", "", "<", "drop_decimal_place")
write("drop_decimal_place", "", ".", "<", "drop_start_marker")
write("drop_start_marker", "", "", "<", "drop_start_marker_")
write("drop_start_marker_", "", "[", ">", "write_zeroes")
for digit in digits+[""]:
    write("nudge_end_marker", digit, digit, ">", "nudge_end_marker")
write("nudge_end_marker", "]", "", ">", "replace_end_marker")
write("replace_end_marker", "", "]", "<", "nudged_end_marker")
write("nudged_end_marker", "", "", "<", "nudged_end_marker")
for digit in digits:
    write("nudged_end_marker", digit, digit, ">", "found_counter")
write("found_counter", "", "", "<", "decrement_digit_counter")

write("write_zeroes", "", "0*", ">", "write_other_zeroes")
write("write_other_zeroes", "", "0", ">", "write_other_zeroes")
write("write_other_zeroes", ".", ".", ">", "write_other_zeroes")
write("write_other_zeroes", "]", "]", "<", "wrote_zeroes")

write("wrote_zeroes", "0", "0", "<", "wrote_zeroes")
write("wrote_zeroes", "0*", "0*", "<", "wrote_zeroes")
write("wrote_zeroes", ".", ".", "<", "wrote_zeroes")
write("wrote_zeroes", "[", "[", "<", "set_up_term_data")

write("set_up_term_data", "", "+", "<", "set_up_term_data_")
write("set_up_term_data_", "", "1", "<", "write_numerator")
write("write_numerator", "", "", "<", "write_numerator_")
write("write_numerator_", "", "4", ">", "perform_division")

#Perform long division
for digit in digits + [""]:
    write("perform_division", digit, digit, ">", "perform_division")
write("perform_division", "+", "+", "<", "take_last_denom_digit")
write("perform_division", "-", "-", "<", "take_last_denom_digit")

for digit in digits:
    write("take_last_denom_digit", digit, "D", "<", "take_last_num_digit_denom_%s" % digit)

for denomDigit in digits:
    for encounteredDigit in digits:
        write("take_last_num_digit_denom_%s" % denomDigit,
              encounteredDigit,
              encounteredDigit,
              "<",
              "take_last_num_digit_denom_%s" % denomDigit)
    write("take_last_num_digit_denom_%s" % denomDigit,
          "",
          "",
          "<",
          "take_last_num_digit_now_denom_%s" % denomDigit)
for denomDigit in digits:
    for numDigit in digits:
        write("take_last_num_digit_now_denom_%s" % denomDigit,
              numDigit,
              "N",
              "<",
              "subtract_num_%s_denom_%s" % (numDigit, denomDigit))

for denomDigit in digits:
    for numDigit in digits:
        for encounteredDigit in digits + ["N"]:
            write("subtract_num_%s_denom_%s" % (numDigit, denomDigit),
                  encounteredDigit,
                  encounteredDigit,
                  "<",
                  "subtract_num_%s_denom_%s" % (numDigit, denomDigit))
        write("subtract_num_%s_denom_%s" % (numDigit, denomDigit),
              "",
              "",
              "<",
              "subtract_num_%s_denom_%s_" % (numDigit, denomDigit))

for denomDigit in digits:
    for numDigit in digits:
        for encounteredDigit in digits:
            write("subtract_num_%s_denom_%s_" % (numDigit, denomDigit),
                  encounteredDigit,
                  encounteredDigit,
                  "<",
                  "subtract_num_%s_denom_%s_" % (numDigit, denomDigit))
        
        difference = int(numDigit) - int(denomDigit)
        if difference >= 0:
            write("subtract_num_%s_denom_%s_" % (numDigit, denomDigit),
                  "",
                  str(difference),
                  ">",
                  "subtracted_num_%s_denom_%s" % (numDigit, denomDigit))
        else:
            write("subtract_num_%s_denom_%s_" % (numDigit, denomDigit),
                  "",
                  str(difference+10),
                  "<",
                  "drop_carry_marker_num_%s_denom_%s" % (numDigit, denomDigit))
        if difference >= 1:
            write("subtract_num_%s_denom_%s_" % (numDigit, denomDigit),
                  "C",
                  str(difference-1),
                  ">",
                  "subtracted_num_%s_denom_%s" % (numDigit, denomDigit))
        else:
            write("subtract_num_%s_denom_%s_" % (numDigit, denomDigit),
                  "C",
                  str(difference+9),
                  "<",
                  "drop_carry_marker_num_%s_denom_%s" % (numDigit, denomDigit))

for denomDigit in digits:
    for numDigit in digits:
        write("drop_carry_marker_num_%s_denom_%s" % (numDigit, denomDigit),
              "",
              "C",
              ">",
              "subtracted_num_%s_denom_%s" % (numDigit, denomDigit))
for denomDigit in digits:
    for numDigit in digits:
        for encounteredDigit in digits + [""]:
            write("subtracted_num_%s_denom_%s" % (numDigit, denomDigit),
                  encounteredDigit,
                  encounteredDigit,
                  ">",
                  "subtracted_num_%s_denom_%s" % (numDigit, denomDigit))
                  
        write("subtracted_num_%s_denom_%s" % (numDigit, denomDigit),
              "N",
              numDigit,
              "<",
              "fetch_num_denom_%s" % denomDigit)
        
    write("subtracted_num_0_denom_%s" % denomDigit,
          "D",
          denomDigit,
          "<",
          "fetch_denom_num_0")

for denomDigit in digits:
    for numDigit in digits:
        write("fetch_num_denom_%s" % denomDigit,
              numDigit,
              "N",
              ">",
              "find_denom_num_%s_denom_%s" % (numDigit, denomDigit))
    write("fetch_num_denom_%s" % denomDigit,
          "",
          "",
          ">",
          "find_denom_num_0_denom_%s" % denomDigit)

for denomDigit in digits:
    for numDigit in digits:
        for encounteredDigit in digits + [""]:
            write("find_denom_num_%s_denom_%s" % (numDigit, denomDigit),
                  encounteredDigit,
                  encounteredDigit,
                  ">",
                  "find_denom_num_%s_denom_%s" % (numDigit, denomDigit))
        
        write("find_denom_num_%s_denom_%s" % (numDigit, denomDigit),
              "D",
              denomDigit,
              "<",
              "fetch_denom_num_%s" % numDigit)

for numDigit in digits:
    for sign in "+-":
        write("find_denom_num_%s_denom_0" % numDigit,
              sign,
              sign,
              "<",
              "fetched_num_%s_denom_0" % numDigit)
    
for numDigit in digits:
    for denomDigit in digits:
        write("fetch_denom_num_%s" % numDigit,
              denomDigit,
              "D",
              "<",
              "fetched_num_%s_denom_%s" % (numDigit, denomDigit))
              
    write("fetch_denom_num_%s" % numDigit,
          "",
          "",
          "<",
          "subtract_num_%s_denom_0" % numDigit)

for denomDigit in digits:
    for numDigit in digits:
        for encounteredDigit in digits:
            write("fetched_num_%s_denom_%s" % (numDigit, denomDigit),
                  encounteredDigit,
                  encounteredDigit,
                  "<",
                  "fetched_num_%s_denom_%s" % (numDigit, denomDigit))
        
        write("fetched_num_%s_denom_%s" % (numDigit, denomDigit),
              "",
              "",
              "<",
              "subtract_num_%s_denom_%s" % (numDigit, denomDigit))

write("subtracted_num_0_denom_0", "+", "+", "<", "check_subtraction_result")
write("subtracted_num_0_denom_0", "-", "-", "<", "check_subtraction_result")

for digit in digits:
    write("check_subtraction_result", digit, digit, "<", "check_subtraction_result")
write("check_subtraction_result", "C", "", ">", "subtraction_negative")
write("check_subtraction_result", "", "", "<", "check_subtraction_result_")

for digit in digits:
    write("check_subtraction_result_", digit, digit, "<", "check_subtraction_result")
write("check_subtraction_result_", "", "", ">", "subtraction_positive")

for digit in digits:
    write("subtraction_negative", digit, "", ">", "subtraction_negative")
write("subtraction_negative", "", "", ">", "multiply_num_by_ten")

for digit in digits:
    write("multiply_num_by_ten", digit ,digit, ">", "multiply_num_by_ten")
write("multiply_num_by_ten", "", "", "<", "multiply_num_0")

for copyingDigit in digits:
    for encounteredDigit in digits:
        write("multiply_num_%s" % copyingDigit,
              encounteredDigit,
              copyingDigit,
              "<",
              "multiply_num_%s" % encounteredDigit)
    
    write ("multiply_num_%s" % copyingDigit,
           "",
           copyingDigit,
           ">",
           "cement_working_digit")

for symbol in digits + ["", "[", "+", "-", "."]:
    write("cement_working_digit", symbol, symbol, ">", "cement_working_digit")

for digit in digits:
    write("cement_working_digit", digit+"*", digit, ">", "create_working_digit")
    
write("create_working_digit", ".", ".", ">", "create_working_digit")

for digit in digits:
    write("create_working_digit", digit, digit+"*", "<", "return_to_subtraction")

write("create_working_digit", "]", "0*", "<", "return_to_subtraction")
write("create_working_digit", "", "", "<", "check_temp_digit")
write("create_working_digit", "!", "", "<", "check_temp_digit_and_continue")

for lowDigit in digits[:5]:
    write("check_temp_digit", lowDigit, "]", "<", "check_for_addition")
write("check_temp_digit", "5", "]", "<", "round_and_continue")
for highDigit in digits[6:]:
    write("check_temp_digit", highDigit, "]", "<", "round")

for lowDigit in digits[:5]:
    write("check_temp_digit_and_continue", lowDigit, "]", "<", "division_complete")
for highDigit in digits[5:]:
    write("check_temp_digit_and_continue", highDigit, "]", "<", "round_and_continue")

for digit in digits:
    write("return_to_subtraction", digit+"*", digit+"*", "<", "return_to_subtraction")
for symbol in digits + [".", "["]:
    write("return_to_subtraction", symbol, symbol, "<", "return_to_subtraction")
write("return_to_subtraction", "+", "+", "<", "take_last_denom_digit")
write("return_to_subtraction", "-", "-", "<", "take_last_denom_digit")

for i, digit in enumerate(digits[:-1]):
    write("round", digit, digits[i+1], "<", "check_for_subtraction")
write("round", "9", "0", "<", "round")
write("round", ".", ".", "<", "round")

for i, digit in enumerate(digits[:-1]):
    write("round_and_continue", digit, digits[i+1], "<", "division_complete")
write("round_and_continue", "9", "0", "<", "round_and_continue")
write("round_and_continue", ".", ".", "<", "round_and_continue")

for digit in digits + [".", "["]:
    write("check_for_addition", digit, digit, "<", "check_for_addition")
write("check_for_addition", "+", "+", ">", "found")
write("check_for_addition", "-", "-", ">", "not_found")

for digit in digits + [".", "["]:
    write("check_for_subtraction", digit, digit, "<", "check_for_subtraction")
write("check_for_subtraction", "+", "+", ">", "not_found")
write("check_for_subtraction", "-", "-", ">", "found")

write("not_found", "[", "[", ">", "reset_working_digit")
for symbol in digits + ["[", "."]:
    write("found", symbol, symbol, ">", "found")
write("found", "]", "", "<", "approximation_complete")

write("subtraction_positive", "", "", ">", "remove_leading_zeroes")
write("remove_leading_zeroes", "0", "#", ">", "remove_leading_zeroes")
for digit in digits[1:]:
    write("remove_leading_zeroes", digit, digit, ">", "find_num")
write("remove_leading_zeroes", "", "", "<", "replace_leading_zero")
write("replace_leading_zero", "#", "0", ">", "find_num")

for digit in digits:
    write("find_num", digit, digit, ">", "find_num")
write("find_num", "", "", ">", "remove_num")

for digit in digits:
    write("remove_num", digit, "", ">", "remove_num")
write("remove_num", "", "", "<", "drop_num_marker")
write("drop_num_marker", "", "@", "<", "copy_subtraction_result")

write("copy_subtraction_result", "", "", "<", "copy_subtraction_result")
write("copy_subtraction_result", "#", "", "<", "copied_subtraction_result")
for digit in digits:
    write("copy_subtraction_result", digit, "", ">", "copying_result_%s" % digit)

for digit in digits:
    write("copying_result_%s" % digit, "", "", ">", "copying_result_%s" % digit)
    write("copying_result_%s" % digit, "@", digit, "<", "drop_num_marker")

write("copied_subtraction_result", "#", "", "<", "copied_subtraction_result")
write("copied_subtraction_result", "", "", ">", "check_sign")

for digit in digits + [""]:
    write("check_sign", digit, digit, ">", "check_sign")
write("check_sign", "@", "", ">", "check_sign")
write("check_sign", "+", "+", ">", "increment_working_digit")
write("check_sign", "-", "-", ">", "decrement_working_digit")

for symbol in digits + ["[", "."]:
    write("increment_working_digit", symbol, symbol, ">", "increment_working_digit")
    for i, digit in enumerate(digits[:-1]):
        write("increment_working_digit", digit+"*", digits[i+1]+"*", ">", "place_change_marker")
    write("increment_working_digit", "9*", "0*", "<", "overflow")

for symbol in digits + ["[", "."]:
    write("decrement_working_digit", symbol, symbol, ">", "decrement_working_digit")
    write("decrement_working_digit", "0*", "9*", "<", "underflow")
    for i, digit in enumerate(digits[1:]):
        write("decrement_working_digit", digit+"*", digits[i]+"*", ">", "place_change_marker")

write("underflow", "0", "9", "<", "underflow")
for i, digit in enumerate(digits[1:]):
    write("underflow", digit, digits[i], ">", "place_change_marker")
write("underflow", ".", ".", "<", "underflow")

for i, digit in enumerate(digits[:-1]):
    write("overflow", digit, digits[i+1], ">", "place_change_marker")
write("overflow", "9", "0", "<", "overflow")
write("overflow", ".", ".", "<", "overflow")

for digit in digits:
    write("place_change_marker", digit+"*", digit+"*", ">", "place_change_marker")
for symbol in digits+["."]:
    write("place_change_marker", symbol, symbol, ">", "place_change_marker")
write("place_change_marker", "", "", "<", "return_to_subtraction")
write("place_change_marker", "!", "!", "<", "return_to_subtraction")
write("place_change_marker", "]", "]", ">", "drop_change_marker")

write("drop_change_marker", "", "!", "<", "placed_change_marker")
write("drop_change_marker", "!", "!", "<", "placed_change_marker")

write("placed_change_marker", "]", "]", "<", "return_to_subtraction")

#Move to next term
for digit in digits:
    write("division_complete", digit, digit, "<", "division_complete")
write("division_complete", ".", ".", "<", "reset_working_digit")
write("division_complete", "[", "[", ">", "reset_working_digit")

for digit in "234":
    write("reset_working_digit", digit, digit+"*", "<", "reset_working_digit")
write("reset_working_digit", "[", "[", "<", "flip_sign")

write("flip_sign", "+", "-", "<", "double_increment_denominator")
write("flip_sign", "-", "+", "<", "double_increment_denominator")

odds = "13579"
for i, digit in enumerate(odds[:-1]):
    write("double_increment_denominator", digit, odds[i+1], "<", "reset_numerator")
write("double_increment_denominator", "9", "1", "<", "increment_denominator")

for i, digit in enumerate(digits[:-1]):
    write("increment_denominator", digit, digits[i+1], "<", "reset_numerator")
write("increment_denominator", "9", "0", "<", "increment_denominator")
write("increment_denominator", "", "1", "<", "denominator_overflow")

for digit in digits:
    write("denominator_overflow", digit, "", "<", "place_four")

for digit in digits:
    write("reset_numerator", digit, digit, "<", "reset_numerator")
write("reset_numerator", "", "", "<", "place_four")

for digit in digits + [""]:
    write("place_four", digit, "4", "<", "wipe_numerator")

for digit in digits:
    write("wipe_numerator", digit, "", "<", "wipe_numerator")
write("wipe_numerator", "", "", ">", "restart_division")

for digit in digits + [""]:
    write("restart_division", digit, digit, ">", "restart_division")
write("restart_division", "+", "+", "<", "take_last_denom_digit")
write("restart_division", "-", "-", "<", "take_last_denom_digit")

for digit in digits + ["."]:
    write("approximation_complete", digit, digit, "<", "approximation_complete")
write("approximation_complete", "[", "\u2248", "<", "drop_pi")

write("drop_pi", "+", "\u03C0", "<", "clean")
write("drop_pi", "-", "\u03C0", "<", "clean")

for digit in digits:
    write("clean", digit, "", "<", "clean")
write("clean", "", "", "<", "clean_")

for digit in digits:
    write("clean_", digit, "", "<", "clean")
write("clean_", "", "", ">", "return")

write("return", "", "", ">", "return")
