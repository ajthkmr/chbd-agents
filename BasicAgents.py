from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]="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"
agent=Agent(
    model=Groq(id="qwen-2.5-32b"),
    description="You are a really good teacher.Please answer based on the questions and keep it concise and clear.Provide examples, 25 model questions with answers, equations and units if applicable.Also recommend what to study next after understanding the current topic",
    tools=[DuckDuckGoTools()],
    markdown=True
)

#question=input("Ask Anything!")
q='''
EAPPLICATIONSOF
CONDUCTORS
Thuscotton prevents the water in theips
AND INSULATORS IN DAILY LIFE
O
from freezing.
An oven is made of double walls and the
Quilts are filled with fluffy cotton.
Airis
spae between them is filled with wool,cork
trapped in the fine pores of cotton.Cotton
etc.The wool and cork are insulators of heat.
They prevent
and air are insulators of heat.
They prevent the heat of the oven to escape
heat from our body to escape and thus keep
Cooking utensils and pans are made
uswarm
of metals such as copper, brass, steel etc.
Newly made quilts are warmer than old ones
The reason is that metals are conductors of
because in old quilts,there is less air trapd
 heat and so they heat up rapidly.)
in the cotton.]
Cooking utensils, pans and tea kettles are
provided with wooden or ebonite handles.
Do you Know?
The wood or the ebonite being insulators of
COn acold daya steel chair feelscolder than a wood
heat, does not pass heat from the utensils to
chair. This is because steel is a good conductor of heat.
our hand. Thus, we can hold the hot utensils
It takes heat from your hand,so you feel cold.Wood is
or pans comfortably by their handles.
an insulator of heat.It doesnot takeheat from your
hand,so you feel warm On the other hand,on a hot day
An ice box is a double-walled box.
The
the steel chair will feel warmer than a wooden chair
space between the walls is filled with cork,
because steel will pass heat from the chair to the hand
glass, wool etc. These filling materials are
while wood willnot.
insulators of heat. They prevent heat from
outside to pass into the ice box.Thus, ice
2.Convection
kept inside the ice box does not melt.
Convection is the process of heat transfer
In summer, ice is kept wrapped in a gunny
by the actual movement of the molecules of the
bag or it is covered with saw dust.The air
medium.Liquids and gases are poor conductors
filled in the fine pores of the gunny bag or
of heat.They are heated mainly by convection
The air does
In solids, the particles do not leave their
saw dust, is insulator of heat.
pass through
so solids are not heated by
not allow heat from outside to
positions,s
it to the ice. Thus, ice is prevented from
convection. In convection, the transfer of heat
is always vertically upwards. The reason being
meltingrapidly.
that the molecules of the medium near the
We use woollen clothes in winter.
Woollen
clothes have fine pores which are filld with
source of heat after absorbing heat start moving
faster, so they move farther i.e. the medium
air. Wool and air are insulators of heat.
expands.As a result, the density of medium near
Therefore, heat from our body does not
the source of heat becomes less i.e. it becomes
escape through them and they keep us warm.
lighter. The less dense medium rises up and the
During very cold weather, water pipes are
denser medium from above moves down to take
covered with cotton.Cotton has air trapped
its place. Thus,a current is set up in the medium
in its fine pores.Cotton and air are insulators
which is called a convection current.
of heat. They do not pass heatfrom the water
77
linside the pipes to the outside atmosphere?
'''
agent.print_response(q)