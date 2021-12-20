exit_code = int(input())
interactor_verdict = int(input())
checker_verdict = int(input())
final_verdict = interactor_verdict

if interactor_verdict == 6:
    final_verdict = 0
elif interactor_verdict == 7:
    final_verdict = 1
elif interactor_verdict == 1:
    final_verdict = checker_verdict
elif interactor_verdict == 0 and exit_code != 0:
    final_verdict = 3
elif interactor_verdict == 0 and exit_code == 0:
    final_verdict = checker_verdict
elif interactor_verdict == 4 and exit_code != 0:
    final_verdict = 3
elif interactor_verdict == 4 and exit_code == 0:
    final_verdict = 4
print(final_verdict)
