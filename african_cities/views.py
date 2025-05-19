from django.shortcuts import render

def city_list(request):
    cities = [
        {
            'name': 'Le Cap',
            'country': 'Afrique du Sud',
            'description': 'Dominée par la majestueuse Table Mountain, Le Cap est une ville cosmopolite où se mêlent plages de sable blanc, vignobles et architecture coloniale. Son front de mer animé et ses quartiers colorés en font une destination incontournable.',
            'image_url': 'https://images.unsplash.com/photo-1584551246679-0daf3d275d0f?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        {
            'name': 'Marrakech',
            'country': 'Maroc',
            'description': 'La "Perle du Sud" enchante par sa médina millénaire, ses souks animés et ses jardins luxuriants. La place Jemaa el-Fna, cœur battant de la ville, offre un spectacle unique de la culture marocaine.',
            'image_url': 'https://images.unsplash.com/photo-1542314831-068cd1dbfeeb?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        {
            'name': 'Zanzibar',
            'country': 'Tanzanie',
            'description': 'Cette île paradisiaque allie plages de sable blanc, eaux turquoise et histoire fascinante. Stone Town, classée au patrimoine mondial de l\'UNESCO, témoigne de son riche passé commercial et culturel.',
            'image_url': 'https://images.unsplash.com/photo-1565967511849-76a60a516170?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        {
            'name': 'Lagos',
            'country': 'Nigeria',
            'description': 'Métropole dynamique et vibrante, Lagos est le cœur économique du Nigeria. Entre ses plages, ses marchés animés et sa scène culturelle florissante, la ville incarne le dynamisme de l\'Afrique moderne.',
            'image_url': 'https://images.unsplash.com/photo-1570129477492-45c003edd2be?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        },
        {
            'name': 'Le Caire',
            'country': 'Égypte',
            'description': 'La "Mère du Monde" fascine par ses pyramides millénaires, son musée égyptien et son souk historique. Cette ville où se côtoient monuments antiques et vie moderne est un véritable musée à ciel ouvert.',
            'image_url': 'https://images.unsplash.com/photo-1572252009286-268acec5ca0a?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80'
        }
    ]
    return render(request, 'african_cities/city_list.html', {'cities': cities}) 