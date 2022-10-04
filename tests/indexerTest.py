import checkpy.tests as t
import checkpy.lib as lib
import checkpy.assertlib as asserts

from _extensions import *


@t.test(0)
def prep_tests(test):
    def testMethod():
        with open("stopwords.txt", "w") as stopwords_file:
            stopwords_file.write(
                "i\nme\nmy\nmyself\nwe\nour\nours\nourselves\nyou\nyour\nyours\nyourself\nyourselves\nhe\nhim\nhis\nhimself\nshe\nher\nhers\nherself\nit\nits\nitself\nthey\nthem\ntheir\ntheirs\nthemselves\nwhat\nwhich\nwho\nwhom\nthis\nthat\nthese\nthose\nam\nis\nare\nwas\nwere\nbe\nbeen\nbeing\nhave\nhas\nhad\nhaving\ndo\ndoes\ndid\ndoing\na\nan\nthe\nand\nbut\nif\nor\nbecause\nas\nuntil\nwhile\nof\nat\nby\nfor\nwith\nabout\nagainst\nbetween\ninto\nthrough\nduring\nbefore\nafter\nabove\nbelow\nto\nfrom\nup\ndown\nin\nout\non\noff\nover\nunder\nagain\nfurther\nthen\nonce\nhere\nthere\nwhen\nwhere\nwhy\nhow\nall\nany\nboth\neach\nfew\nmore\nmost\nother\nsome\nsuch\nno\nnor\nnot\nonly\nown\nsame\nso\nthan\ntoo\nvery\ns\nt\ncan\nwill\njust\ndon\nshould\nnow\nwould\none\ntwo\nthree\nlike\nlong\nus\ncould\nsee\nmust\nsaid\n"
            )
        with open("test.txt", "w") as test_file:
            test_file.write(
                "Riggan stares into the mirror, in the reflection he catches\nsight of a poster from a movie called 'Birdman 3'. The\nsuperhero, Birdman (a younger Riggan in a bird costume), wings\nwidely spread, stares directly back at him. A hand written\nnote on the top of the poster reads: 'Thomson, break a wing!\nFrom the boys at Local 1.' Riggan tries to calm himself with a\nmantra...\n\n                    RIGGAN\n          'Breathing in, I embrace my anger.\n          Breathing out, I smile to it.'\n\n                                                    (CONTINUED)\n                                                10/29/14   /   10.\n\n                    BIRDMAN (V.O.)\n          Embrace it. Kiss it. Turn it around and\n          fuck it in the--\n\nA knock on the door behind him.\n\n                      RIGGAN\n          Not now!\n\nLaura opens the door and sticks her head in.\n                    LAURA\n          Can I come in?\n\n                      RIGGAN\n          No.\n\n                    LAURA\n          Okay. Two words. Shia La Beouf.\n\n                    RIGGAN\n          That's three words.\n\n                      LAURA\n          It's two.\n\n                      RIGGAN\n          Get out.\n\n                    LAURA\n          I love you.\n\nShe closes the door. Riggan tries to calm himself down, but\nLaura opens the door again.\n\n                    LAURA (CONT'D)\n          I take it we're not going to dinner\n          anymore?\n\n                    RIGGAN\n          I don't have an actor.\n                    LAURA\n          I don't have a life.\n\n                      RIGGAN\n          Laura...\n\n                    LAURA\n          Fine. Whatever.\n              (Goes to leave but stops.)\n          You remember at Joan's when you\n          asked me to come do a Broadway play\n          with you? You said it would be\n          fun...\n                                                    (CONTINUED)\n                                                  10/29/14     /   11.\n\n                          RIGGAN\n               Go away.\n\n                         LAURA\n               So far? No fun.\n\n     Riggan closes the door and looks at the Birdman poster.\n\n                         BIRDMAN (V.O.)\n               Fun? You know what would be fun? Getting\n               the fuck out of here before we humiliate\n               ourselves. That would be fun.\n\n     Riggan looks at himself in the mirror and begins to pull at\n     his hair. As it comes off his head, we discover it was a wig.\n     He turns away from the mirror, trying desperately to stay\n     calm. Something catches his eye: a vase of roses on the end\n     of the table. A card in them says, 'They didn't have the\n     whatever you wanted - Sam'. Enraged, Riggan focuses on the\n     vase. It begins to shift. Then, with a surge of anger,\n     without ever touching it, he sends it crashing against the\n     wall on the other side of the room.\n\n     The camera pans over the roses scattered across the floor. It\n     hovers over the carpet and around the perimeter of the room,\n     until it finally settles on Riggan, now dressed in a casual\n     blazer.\n\nA5                                                                 A5\n\n     It is later the same day. He is sitting on the sofa and on three\n     chairs in front of him are three journalists:\n\n     Gabriel, a geeky theatre journalist, wearing thick glasses and\n     a thin tie. Clara, a reporter from an entertainment blog. And\n     Han, a polite, obese Japanese journalist, who sits next to his\n     translator, another Japanese guy.\n\n                         GABRIEL\n               Why does somebody go from playing the lead\n               in a comic book franchise to adapting\n               Raymond Carver for the stage?\n\n     Riggan tries to remain calm.\n\n                         GABRIEL (CONT'D)\n               I mean, as you're probably aware, Barthes\n               said, 'The cultural work done in the past\n               by gods and epic sagas is now done by\n               laundry detergent commercials and comic\n               strip characters.' It's a big leap you've\n               taken...\n\n     Riggan shifts nervously.\n                                                          (CONTINUED)\n                                                10/29/14   /   12.\n\n                    RIGGAN\n          Well... Absolutely. As you said... that\n          Barthes said... Birdman, like Icarus...\n\n                    CLARA\n          Hang on. Who's this Barthes guy? Which\n          Birdman was he in?\n\n                    GABRIEL\n          Roland Barthes was a French philosopher,\n          who--\n                    CLARA\n          Oh. Okay. Sure. Now, is it true you've been\n          injecting yourself with semen from baby\n          pigs?\n\n                    RIGGAN\n          What?\n\n                    CLARA\n          As a method of facial rejuvenation.\n\n                    RIGGAN\n          Who told you that?\n\n                    CLARA\n          It was tweeted by... (checks her notes)\n          @prostatewhispers.\n\n                    RIGGAN\n          It's a lie.\n\n                    CLARA\n          I know. But did you do it?\n\n                    RIGGAN\n          No!\n\n                    GABRIEL\n          Are you afraid at all that people will say\n          you're doing this play to battle the\n          impression that you're a washed-up super\n          hero?\n\n                     RIGGAN\n          No. I'm not. And that's exactly why\n          20 years ago I refused to do\n          Birdman 4.\n\n                    HAN\n          Birdman 4??? You do Birdman 4???\n\nJake opens the door and the camera pans to him.\n\n                                                     (CONTINUED)\n                                                10/29/14   /   13.\n\n10   INT. HALLWAY - THEATER - CONTINUOUS                            10\n     ...through the hallway. He walks by Jake and Riggan who are mid\n     conversation. We stay with them.\n\n\n\n                         RIGGAN (O.S.)\n               I don't care, sign it.\n                         JAKE (O.S.)\n               Listen to me.\n\n                         RIGGAN (O.S.)\n               No you listen to me--\n\n                         JAKE (O.S.)\n               I can't afford to listen to you...\n\n                         LARRY\n               I'm gonna need to go shopping\n               again.\n\n                         JAKE\n               Fucking sew something, you old\n               fuck!\n\n                         RIGGAN\n               I don't care. Give him what he\n               wants.\n                         JAKE\n               His agent is asking for almost four\n               times what we were paying--\n\n                         RIGGAN\n               Then go into the reserve.\n\n                         JAKE\n               The reserve is gone. You spent it\n               on the fog. And those fake trees...\n                                                         (CONTINUED)\n                                               10/29/14   /   27.\n\n                    RIGGAN\n          It's a dream sequence, it--\n\n                    JAKE\n          And three union midgets that dance\n          around like--\n\n                    RIGGAN\n          You're not supposed to call them\n          midgets--\n                    JAKE\n          The reserve is gone!\n\n                    RIGGAN\n          Listen to me, you didn't see what I\n          just saw. But you will, at the preview\n          tomorrow. Look, get the contract done.\n          I'll get the money.\n\nRiggan begins marching toward the stage.\n                    JAKE\n              (Calling after him.)\n          When???\n\nLaura comes down some stairs and chases Riggan.\n\n                    LAURA\n              (Incredulous.)\n          Hey, is it true? Shiner?\n\n                     RIGGAN\n          He's in.\n\n                    LAURA\n          Holy shit! When can I meet him?\n\n                    RIGGAN\n          He's in a fitting with Larry.\nLesley comes down the hallway.\n\n                    LESLEY\n          I'm going to Starbucks. You guys\n          want anything?\n\n                    RIGGAN\n          I'm fine. How's Mike?\n\n                    LESLEY\n          Did you talk to your daughter?\n\n                     RIGGAN\n          No.\n                                                   (CONTINUED)\n                                                     10/29/14   /    28.\n\n                          LESLEY\n                He's great.\n\n                          LAURA\n                    (To Lesley. Matter-of-\n                     factly.)\n                Honey, your tits look like fucking\n                anjou pears in that top!\n\n                          LESLEY\n                    (Uncomfortable.)\n                Okay, well I'm gonna-- Thank you.\n\n      She walks away.\n\n                          LAURA\n                And that ass. Like two eggs in a hanky!\n\nA10                                                                 A10\n\n      Riggan walks, Laura follows him.\n\n                          LAURA\n                Okay, I was going to tell you this over\n                dinner, but everything-- I have some news\n                too.\n                          RIGGAN\n                Good or bad? Cause right now--\n\n      A technician walks by.\n\n                          LAURA\n                    (Whispering.)\n                I missed my last two periods.\n                    (Beat.)\n                I think it's happening this time.\n\n      Riggan stops. Silent. A beat.\n\n                           LAURA (CONT'D)\n                Is that good or bad?\n                    (He stares at her.)\n                Riggan...?\n\n                          RIGGAN\n                It's good. It's great.\n      She smiles, her eyes filled with emotion. Riggan smiles back,\n      and nods absently.\n\n                          LAURA\n                Say something else...\n\n                                                          (CONTINUED)\n                                                     10/29/14   /   29.\n\n                         RIGGAN\n                   (Joking.)\n               You're pretty sure it's mine?\n\n                         LAURA\n                   (Unamused but plays along)\n               Well, let's see. There's you. Jake. That\n               masseuse wore a condom so... Yes, it's\n               yours... idiot.\n\n     She puts her head on Riggan's chest. We see his mind racing.\n     Laura is moved, and confused.\n\n                         LAURA (CONT'D)\n               Are you excited?\n\n                         RIGGAN\n               Yeah.\n\n                         LAURA\n               Me too.\n     Laura moves slightly away from him and suddenly slaps him across\n     the face. Riggan looks at her, confused.\n\n                         RIGGAN\n               What--?\n\n                         LAURA\n               You're not funny.\n\n     She kisses him intensely on the lips and briefly places his\n     hand on her belly, then moves it up to her breasts. After a\n     moment, she backs away.\n\n                         LAURA (CONT'D)\n               First preview tomorrow. Here we go!\n\n     Laura turns and walks away. Riggan continues down the\n     corridor. He passes by a Security Guard· in front of a small\n     TV. The camera becomes Riggan's POV and advances until...\n\n11   INT. BACKSTAGE - THEATER - EVENING                             11\n\n     ...we go through the stage door. We scan the backstage area to\n     see the stagehands ready to do their jobs. We can feel the\n     electricity of a first preview.\n\n     On stage part of the kitchen set from before is visible. Annie\n     stands at her podium, calling the cues for the show.\n\n                         ANNIE\n                   (Into her headset.)\n               Cue 34 and 35. Go.\n                                                          (CONTINUED)\n                                                10/29/14   /   30.\n\nShe turns and looks directly into the camera.\n\n                       ANNIE (CONT'D)\n          Places.\n\n                       RIGGAN (O.S.)\n          Okay.\n\nRiggan walks on screen wearing his costume, carrying a bucket of\nice and a bottle of gin. He goes to the opposite side of the\nstage and takes his place in the wings. He peeks out at the\naudience who seem to be watching with interest.\n\nThen we pan to the stage to find Mike, Lesley and Laura\nperforming the scene we saw at the beginning, around the table.\nMike looks comfortable, sipping at his drink. A half empty\nbottle of gin on the table.\n\n                    MIKE\n          The maniac shot himself right in front of\n          us. I rode with him in the ambulance to the\n          hospital.\n\n                    LESLEY\n          I'll never get that image out of my head.\n          Right before he did it, his eyes-- they\n          were so sad... lonely.\n\n                    LAURA\n          Did you have to treat him?\n\n                    MIKE\n          I didn't have to. But I did.\n              (Pouring another drink.)\n          He was in bad shape. His head swelled\n          up to like twice the size of a normal\n          head. I'd never seen anything like\n          it. And I swear to God, I hope I\n          never do again.\n\nRiggan stands near Annie.\n                       RIGGAN\n          He's good.\n\n                    ANNIE\n          He's incredible. I think he's\n          drinking real gin.\n"
            )

        return asserts.fileExists(test.fileName)

    test.test = testMethod
    test.description = lambda: "File exists."


@t.test(1)
def checks_type(test):
    def testMethod():
        fn = lib.getFunction("create_index", test.fileName)
        index = fn("stopwords.txt", [])
        if len(index) != 138:
            return False, "The index does not include all words."

        for key, value in index.items():

            if not isinstance(key, str):
                return False, "Keys in index should be strings."

            if not isinstance(value, list):
                return False, "Values of the index should be lists."

            try:
                if not isinstance(value[0], int):
                    return False, "Values of the index should be lists of integers."
            except:
                return (
                    False,
                    "Values of the index should be non-empty lists of integers.",
                )

        return True

    test.test = testMethod
    test.description = lambda: "'create_index' returns the correct type and data."


@t.test(2)
def checks_tekst1(test):
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            argv=["indexer.py", "test.txt"],
            stdinArgs=["dinner", ""],
            overwriteAttributes=[("__name__", "__main__")],
        )

        return re.search(r".*dinner.*51, 306", output)

    test.test = testMethod
    test.description = (
        lambda: "Finds the word 'dinner' on lines 51 and 306 in a modified text file."
    )


@t.test(3)
def checks_crash(test):
    def testMethod():
        output = lib.outputOf(
            test.fileName,
            argv=["indexer.py", "test.txt"],
            stdinArgs=["women", "dinner", ""],
            overwriteAttributes=[("__name__", "__main__")],
        )
        return re.search(r".*dinner.*51, 306", output)

    test.test = testMethod
    test.description = lambda: "Allows for another search if a word is not found."
