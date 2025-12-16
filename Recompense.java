public class Recompense {
    private String nom;
    private int bonusXp;

    private Quete quete;

    public Recompense(String nom, int bonusXp) {
        this.nom = nom;
        this.bonusXp = bonusXp;
    }

    public String getNom() { return nom; }
    
    public int getBonusXp() { return bonusXp; }

    public Quete getQuete() { return quete; }
    
    void setQueteInternal(Quete q) { this.quete = q; }
}
