export type ClassroomExercise = {
  id: string;
  instruction: string;
  prompt: string;
  options: string[];
  answer: string;
  explanation: string;
};

export const demoClassroomExercise: ClassroomExercise = {
  id: "verb-to-be-introduction",
  instruction: "Complete a apresentação com a forma correta do verbo to be.",
  prompt: "Hello! I ___ from Brazil.",
  options: ["am", "is", "are"],
  answer: "am",
  explanation: "Usamos “am” com o pronome “I”: I am from Brazil.",
};

export function checkClassroomAnswer(exercise: ClassroomExercise, answer: string) {
  return answer.trim().toLocaleLowerCase("en") === exercise.answer.toLocaleLowerCase("en");
}
