public class Quete {
    private String titre;
    private int xp;
    private Recompense recompense;


    public Quete(String titre) {
        this.titre = titre;
        this.xp = 0;
    }
    

    public String getTitre() { return titre; }
    public int getXp() { return xp; }

    public void setTitre(String titre) { this.titre = titre; }

    public void ajouterXp(int points) {
        if (points <= 0) return;
        xp += points;
    }
    
    public Recompense getRecompense() { return recompense; }
    
    public int xpTotalAvecBonus() {
        if (recompense == null) return xp;
        return xp + recompense.getBonusXp();
    }

    public void attribuerRecompense(Recompense nouvelle) {
        if (this.recompense == nouvelle) return;
    
        // détacher l'ancienne
        if (this.recompense != null) {
            Recompense ancienne = this.recompense;
            this.recompense = null;
            ancienne.setQueteInternal(null);
        }
    
        // attacher la nouvelle
        this.recompense = nouvelle;
        if (nouvelle != null) {
            Quete ancienneQuete = nouvelle.getQuete();
            if (ancienneQuete != null && ancienneQuete != this) {
                ancienneQuete.attribuerRecompense(null);
            }
            nouvelle.setQueteInternal(this);
        }
    }

    
}
