from rest_framework import serializers


class LessonSummarySerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    skill = serializers.CharField()
    summary = serializers.CharField()
    estimatedMinutes = serializers.IntegerField()
    xpReward = serializers.IntegerField()
    position = serializers.IntegerField()


class CourseUnitSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    position = serializers.IntegerField()
    lessons = LessonSummarySerializer(many=True)


class CourseOutlineSerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    description = serializers.CharField()
    level = serializers.CharField()
    lessonCount = serializers.IntegerField()
    units = CourseUnitSerializer(many=True)


class CourseSummarySerializer(serializers.Serializer):
    slug = serializers.SlugField()
    title = serializers.CharField()
    description = serializers.CharField()
    level = serializers.CharField()
    unitCount = serializers.IntegerField()
    lessonCount = serializers.IntegerField()


class LessonChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    position = serializers.IntegerField()


class LessonQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    type = serializers.CharField()
    prompt = serializers.CharField()
    position = serializers.IntegerField()
    choices = LessonChoiceSerializer(many=True, required=False)
    tokens = serializers.ListField(child=serializers.CharField(), required=False)
    audioText = serializers.CharField(required=False)


class DialogueLineSerializer(serializers.Serializer):
    speaker = serializers.CharField()
    line = serializers.CharField()


class LessonDetailSerializer(LessonSummarySerializer):
    unit = serializers.CharField()
    theory = serializers.CharField()
    example = serializers.CharField()
    keyPoints = serializers.ListField(child=serializers.CharField())
    dialogue = DialogueLineSerializer(many=True, required=False)
    passingPercent = serializers.IntegerField()
    questions = LessonQuestionSerializer(many=True)


class AnswerRequestSerializer(serializers.Serializer):
    questionId = serializers.IntegerField()
    choiceId = serializers.IntegerField(required=False)
    answer = serializers.CharField(required=False, allow_blank=True)
    order = serializers.ListField(
        child=serializers.CharField(), required=False, allow_empty=True
    )


class AnswerFeedbackSerializer(serializers.Serializer):
    isCorrect = serializers.BooleanField()
    explanation = serializers.CharField()
    selectedChoiceId = serializers.IntegerField(required=False)
    correctChoiceId = serializers.IntegerField(required=False)
    correctAnswer = serializers.CharField(required=False)
