import setting as st
import star as s


def main():
    run = True
    clock = st.pygame.time.Clock()

    li_test = []
    for i in range(1, 500):
        li_test.append(s.Star())
    s.Star.show_xy()

    while run:
        clock.tick(12)

        st.WIN.fill((0, 0, 0))
        st.pygame.display.update()

        # Pętla do obsługi zdarzeń
        for event in st.pygame.event.get():
            if event.type == st.pygame.QUIT:
                run = False

        for star in li_test:
            star.update_color()
            star.update_position()
            star.draw(st.WIN)  #polar2.draw(WIN)
        st.pygame.display.update()

    st.pygame.quit()


main()
