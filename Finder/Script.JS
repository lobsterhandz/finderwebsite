$(document).ready(function() {
    let currentLoadedProfiles = 0;
    const profilesToLoad = 12;
    const detaMicroURL = 'https://<your-deta-micro-url>/profiles';

    function loadMoreProfiles() {
        $.ajax({
            url: detaMicroURL,
            data: {
                page: Math.ceil(currentLoadedProfiles / profilesToLoad)
            },
            success: function(data) {
                const profiles = data.profiles;
                for (let i = 0; i < profiles.length; i++) {
                    const profile = profiles[i];
                    const card = `
                        <div class="bg-gray-800 rounded-lg overflow-hidden shadow">
                            <img src="${profile.image}" alt="${profile.name}" class="w-full h-64 object-cover">
                            <div class="p-4">
                                <h2 class="text-2xl font-bold"><a href="${profile.url}" target="_blank" class="text-blue-500 hover:text-blue-600">${profile.name}</a></h2>
                                <div class="mt-2">
                                    <span class="text-gray-500">Likes: ${profile.likes} <i class="fas fa-heart"></i></span>
                                    <span class="text-gray-500">Subscribers: ${profile.subscribers} <i class="fas fa-play mr-2"></i></span>
                                </div>
                            </div>
                        </div>
                    `;

                    $('#profiles').append(card);
                    currentLoadedProfiles++;
                }
            }
        });
    }

    function searchProfiles() {
        currentLoadedProfiles = 0;
        $('#profiles').empty();
        loadMoreProfiles();
    }

    function handleScroll() {
        const scrollTop = $(window).scrollTop();
        const windowHeight = $(window).height();
        const documentHeight = $(document).height();
        const threshold = 200;

        if (scrollTop + windowHeight >= documentHeight - threshold) {
            loadMoreProfiles();
        }
    }

    loadMoreProfiles();

    $("#searchBtn").click(searchProfiles);

    $(window).scroll(handleScroll);
});
