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


class LessonChoiceSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    position = serializers.IntegerField()


class LessonQuestionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    prompt = serializers.CharField()
    position = serializers.IntegerField()
    choices = LessonChoiceSerializer(many=True)


class LessonDetailSerializer(LessonSummarySerializer):
    unit = serializers.CharField()
    theory = serializers.CharField()
    example = serializers.CharField()
    keyPoints = serializers.ListField(child=serializers.CharField())
    passingPercent = serializers.IntegerField()
    questions = LessonQuestionSerializer(many=True)


class AnswerRequestSerializer(serializers.Serializer):
    questionId = serializers.IntegerField()
    choiceId = serializers.IntegerField()


class AnswerFeedbackSerializer(serializers.Serializer):
    isCorrect = serializers.BooleanField()
    selectedChoiceId = serializers.IntegerField()
    correctChoiceId = serializers.IntegerField()
    explanation = serializers.CharField()
