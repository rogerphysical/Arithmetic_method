def convertTabs(code, x):
  return (" "*x).join([code[([0]+[i+1 for i in range(len(code)) if code[i] =='\t'])[x]:([i for i in range(len(code)) if code[i] =='\t']+[len(code)+1])[x]] for x in range(len([i for i in range(len(code)) if code[i] =='\t']+[-1]))])
