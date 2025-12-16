import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.*;

public class QueteTest {

    private Quete quete;
    private Recompense recompense;

    @BeforeEach
    public void setUp() {
        quete = new Quete("Sauver le village");
        recompense = new Recompense("Sac d’or", 20);
        quete.attribuerRecompense(recompense);
    }

    @Test
    public void ajouterXp_augmenteXp() {
        quete.ajouterXp(10);
        assertEquals(10, quete.getXp());
    }

    @Test
    public void xpTotalAvecBonus_utiliseRecompense() {
        quete.ajouterXp(10);
        assertEquals(30, quete.xpTotalAvecBonus());
    }

    @Test
    public void ajouterXp_ignoreValeursInvalides() {
        quete.ajouterXp(-5);
        quete.ajouterXp(0);
        assertEquals(0, quete.getXp());
    }
    
    @Test
    public void uneRecompenseNePeutAvoirQuUneQuete() {
        Quete q1 = new Quete("Q1");
        Quete q2 = new Quete("Q2");
        Recompense r = new Recompense("Couronne", 50);
    
        q1.attribuerRecompense(r);
        q2.attribuerRecompense(r);
    
        assertNull(q1.getRecompense());
        assertEquals(r, q2.getRecompense());
        assertEquals(q2, r.getQuete());
    }
}
