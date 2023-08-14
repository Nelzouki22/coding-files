def mad_libs():
    # The story template with blanks
    story = "Once upon a time, in a [adjective] [noun], there lived a [adjective] [noun]. " \
            "One day, they decided to [verb] to the [noun] to [verb] some [plural_noun]. " \
            "But suddenly, a [adjective] [noun] appeared and [verb] all the [plural_noun]! " \
            "The [noun] was in [adjective] despair, but then a [adverb] [noun] came to the rescue " \
            "and [verb] the [adjective] [noun] away. Everyone lived [adverb] ever after."

    # Ask the user for input words
    adjective1 = input("Enter an adjective: ")
    noun1 = input("Enter a noun: ")
    adjective2 = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    verb1 = input("Enter a verb: ")
    noun3 = input("Enter a noun: ")
    verb2 = input("Enter a verb: ")
    plural_noun1 = input("Enter a plural noun: ")
    adjective3 = input("Enter an adjective: ")
    noun4 = input("Enter a noun: ")
    adverb1 = input("Enter an adverb: ")
    noun5 = input("Enter a noun: ")
    verb3 = input("Enter a verb: ")
    adjective4 = input("Enter an adjective: ")
    adverb2 = input("Enter an adverb: ")

    # Fill in the blanks in the story
    filled_story = story.replace("[adjective]", adjective1).replace("[noun]", noun1) \
                       .replace("[adjective]", adjective2).replace("[noun]", noun2) \
                       .replace("[verb]", verb1).replace("[noun]", noun3) \
                       .replace("[verb]", verb2).replace("[plural_noun]", plural_noun1) \
                       .replace("[adjective]", adjective3).replace("[noun]", noun4) \
                       .replace("[adverb]", adverb1).replace("[noun]", noun5) \
                       .replace("[verb]", verb3).replace("[adjective]", adjective4) \
                       .replace("[adverb]", adverb2)

    print("\nHere's your Mad Libs story:\n")
    print(filled_story)

# Run the Mad Libs generator
mad_libs()
