from src.PlanificationAlgorithms.Priority import Priority

class PreemptivePriority(Priority):

    def mustExpropiate(self, currentPcb, anotherPcb):
        return currentPcb.getPriority() > anotherPcb.getPriority()
