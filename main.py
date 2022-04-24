import setting as st
import star as s


def main():

    run = True
    clock = st.pygame.time.Clock()

    # Generowanie układu gwiazd
    li_test = []
    for i in range(1, 500):
        li_test.append(s.Star())
    s.Star.show_xy()    # Podgląd współrzędnych
    kometa = s.Comet()

    steper = 0  # Prędkość obiektów

    while run:

        clock.tick(st.CLOCK_TICKS)
        st.WIN.fill((0, 0, 0))

        # Pętla do obsługi zdarzeń
        for event in st.pygame.event.get():
            if event.type == st.pygame.QUIT:
                run = False

        # Pętla do aktualizacji obiektów gwiazd
        for star in li_test:
            st.check_step(steper, 2, star.update_color)
            st.check_step(steper, 5, star.update_position)  # Dzielnik prędkości
            star.draw(st.WIN)

        # Pętla do aktualizacji komet
        kometa.update_position()
        kometa.draw(st.WIN)

        st.pygame.display.update()
        steper = st.n_step(steper)

    st.pygame.quit()


main()



