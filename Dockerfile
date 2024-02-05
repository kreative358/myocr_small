FROM docker.io/pytorch/pytorch

# if you forked myocr_small, you can pass in your own GitHub username to use your fork
# i.e. gh_username=myname
# ARG gh_username=JaidedAI
ARG gh_username=kreative358
# ARG service_home="/home/myocr_small"
ARG service_home="/home/myocr_small"

# Configure apt and install packages
RUN apt-get update -y && \
    apt-get install -y \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    libgl1-mesa-dev \
    git \
    # cleanup
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists

# Clone myocr_small repo
RUN mkdir "$service_home" \
    # && git clone "https://github.com/$gh_username/myocr_small.git" "$service_home" \
    && git clone "https://github.com/$gh_username/myocr_small.git" "$service_home" \
    && cd "$service_home" \
    # && git remote add upstream "https://github.com/JaidedAI/myocr_small.git" \
    && git remote add upstream "https://github.com/kreative358/myocr_small.git" \
    && git pull upstream master

# Build
RUN cd "$service_home" \
    && python setup.py build_ext --inplace -j 4 \
    && python -m pip install -e .
