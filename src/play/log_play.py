from cf import logger


def main():

    logger.trace("Hello, world!")
    logger.debug("Hello, world!")
    logger.info("Hello, world!")
    logger.success("Hello, world!")
    logger.warning("Hello, world!")
    logger.error("Hello, world!")
    logger.critical("Hello, world!")


if __name__ == "__main__":
    main()
