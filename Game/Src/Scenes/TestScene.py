from Engine import *

class TestScene(Scene):
  def __init__(self):
    super().__init__()


    self.addEntity(Dragable(100,100,100,50,"TEST"))
    self.addEntity(Button(300,100,100,50,"TEST", PrintCommand("button pressed")))


    # add animated test entity 
    e = Entity()
    trans = TransformComponent(e, 100, 200)
    anim = AnimatedComponent(e)
    animFinTrigger = PrintCommand("AnimationFinishTrigger")
    anim.setAnimationFinishTrigger(animFinTrigger)

    click = ClickableComponent(e, 50,50)
    drag = DragComponent(e)
    command = CommandComponent(e)


    e.add_component(trans)
    e.add_component(anim)
    e.add_component(click)
    e.add_component(drag)
    e.add_component(command)

    self.addEntity(e)
